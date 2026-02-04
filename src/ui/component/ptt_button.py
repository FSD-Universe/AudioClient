from typing import Optional

from PySide6.QtCore import QObject, Signal


class PTTButton(QObject):
    """
    简单的 PTT 状态管理器。

    增加了时间消抖逻辑，防止某些硬件或驱动在极短时间内产生
    多次按下/松开事件，导致 PTT 快速抖动。
    """

    ptt_pressed = Signal(bool)

    def __init__(
        self,
        debounce_interval_ms: int = 80,
    ) -> None:
        """
        :param debounce_interval_ms: 状态变化之间的最小间隔（毫秒）,
                                     默认 80ms 基本不会影响正常按键。
        """
        super().__init__()
        self._target_key: Optional[str] = None
        self._ptt_active: bool = False
        self._debounce_interval_ms: int = debounce_interval_ms
        self._last_press_ms: Optional[float] = None

    def set_target_key(self, target_key: str) -> None:
        self._target_key = target_key

    def set_debounce_interval(self, debounce_interval_ms: int) -> None:
        """运行时调整消抖时间。"""
        self._debounce_interval_ms = max(0, int(debounce_interval_ms))

    def _can_activate(self) -> bool:
        """
        按下沿消抖：两次「激活」之间至少间隔 _debounce_interval_ms 毫秒。

        只对从未按下 -> 按下的边沿做消抖，
        松开时不做时间限制，避免短按变成“锁定”效果。
        """
        import time

        now_ms = time.monotonic() * 1000.0
        if self._last_press_ms is None:
            self._last_press_ms = now_ms
            return True

        if now_ms - self._last_press_ms < self._debounce_interval_ms:
            # 间隔太短，认为是抖动，忽略本次“按下”
            return False

        self._last_press_ms = now_ms
        return True

    def key_pressed(self, key: str) -> None:
        if self._target_key is None:
            return
        if not self._ptt_active and key == self._target_key and self._can_activate():
            self._ptt_active = True
            self.ptt_pressed.emit(self._ptt_active)

    def key_released(self, key: str) -> None:
        if self._target_key is None:
            return
        if self._ptt_active and key == self._target_key:
            self._ptt_active = False
            self.ptt_pressed.emit(self._ptt_active)
