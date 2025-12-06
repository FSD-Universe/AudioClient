from time import time

from PySide6.QtCore import QObject, QTimer, Signal


class Receiver(QObject):
    receiving = Signal(bool)
    received = Signal()

    def __init__(self, check_interval: int, /):
        super().__init__()
        self.last_received = -1
        self._under_receiving = False
        self.check_interval = check_interval / 1000
        self.timer = QTimer()
        self.timer.timeout.connect(self._timer_handler)
        self.timer.setInterval(check_interval)
        self.received.connect(self._receive_handler)

    def _receive_handler(self):
        if self._under_receiving:
            return
        self._under_receiving = True
        self.receiving.emit(True)
        self.last_received = time()

    def _timer_handler(self):
        if time() - self.last_received > self.check_interval:
            self.receiving.emit(False)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()
