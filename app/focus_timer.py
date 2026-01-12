from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIntValidator


class FocusTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.time_left = 25 * 60
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)

        self.timerTextBox = QLineEdit()
        self.timerTextBox.setValidator(QIntValidator(0, 999))

        self.label = QLabel("25:00")
        self.label.setStyleSheet("font-size: 26px;")

        start = QPushButton("Start")
        reset = QPushButton("Reset")
        self.setTimeButton = QPushButton("Set Timer")

        start.clicked.connect(self.start)
        reset.clicked.connect(self.reset)
        self.setTimeButton.clicked.connect(self.setTime)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.timerTextBox)
        hlayout.addWidget(self.setTimeButton)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(start)
        hlayout2.addWidget(reset)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addLayout(hlayout)
        layout.addLayout(hlayout2)

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

    def setTime(self):
        text = self.timerTextBox.text()

        if not text:
            return  # do nothing if empty

        minutes = int(text)
        self.time_left = minutes * 60
        self.timer.stop()
        self.update_label()

