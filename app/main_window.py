from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt
from .task_manager import TaskManager
from .focus_timer import FocusTimer
from .motivation import MotivationWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eggy")
        self.resize(900, 500)

        central = QWidget()
        layout = QHBoxLayout(central)

        left = QVBoxLayout()
        left.addWidget(TaskManager())
        left.addWidget(FocusTimer())

        layout.addLayout(left)
        layout.addWidget(MotivationWidget(), alignment=Qt.AlignBottom | Qt.AlignRight)

        self.setCentralWidget(central)
