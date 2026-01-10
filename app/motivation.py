import random
from pathlib import Path
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap


class MotivationWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.folder: Path | None = None

        self.image = QLabel("No \"Motivational Image\" folder.")
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setFixedSize(200, 120)

        self.pick_btn = QPushButton("Pick a \"Motivational Image\" folder")
        self.pick_btn.clicked.connect(self.pick_folder)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(5 * 60 * 1000)

        layout = QVBoxLayout(self)
        layout.addWidget(self.image)
        layout.addWidget(self.pick_btn)

    def pick_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self, "Pick \"Motivational Image\" Folder"
        )
        if folder:
            self.folder = Path(folder)
            self.update_image()

    def update_image(self):
        if not self.folder:
            return

        images = (
            list(self.folder.glob("*.png")) +
            list(self.folder.glob("*.jpg")) +
            list(self.folder.glob("*.jpeg"))
        )

        if not images:
            self.image.setText("No images found")
            return

        pixmap = QPixmap(str(random.choice(images)))
        self.image.setPixmap(
            pixmap.scaled(
                self.image.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )
