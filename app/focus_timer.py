from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer


class FocusTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.time_left = 25 * 60
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)

        self.label = QLabel("25:00")
        self.label.setStyleSheet("font-size: 32px;")

        start = QPushButton("Start")
        reset = QPushButton("Reset")

        start.clicked.connect(self.start)
        reset.clicked.connect(self.reset)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(start)
        layout.addWidget(reset)

    def start(self):
        self.timer.start(1000)

    def reset(self):
        self.timer.stop()
        self.time_left = 25 * 60
        self.update_label()

    def tick(self):
        self.time_left -= 1
        self.update_label()
        if self.time_left <= 0:
            self.timer.stop()

    def update_label(self):
        m, s = divmod(self.time_left, 60)
        self.label.setText(f"{m:02}:{s:02}")
