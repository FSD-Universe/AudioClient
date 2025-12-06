from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton


class SelectedButton(QPushButton):
    button_active = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._set_deactivate_style()
        self._active = False
        self.clicked.connect(self._button_click)

    def _button_click(self):
        self._active = not self._active
        self.button_active.emit(self._active)
        if self._active:
            self._set_activate_style()
        else:
            self._set_deactivate_style()

    def _set_activate_style(self):
        self.setStyleSheet("background-color: rgb(111, 255, 116);color: black;")

    def _set_deactivate_style(self):
        self.setStyleSheet("background-color: rgb(189, 189, 189);color: black;")

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool):
        self._active = value
        if value:
            self._set_activate_style()
        else:
            self._set_deactivate_style()
