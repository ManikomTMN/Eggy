import sys
import platform
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from app.main_window import MainWindow

app = QApplication(sys.argv)

current_os = platform.system()
if current_os == "Windows":
    icon_path = "assets/egg_icon.ico"
elif current_os == "Darwin":  # macOS
    icon_path = "assets/egg_icon.icns"
else:  # Linux / other
    icon_path = "assets/egg_icon.png"

app.setWindowIcon(QIcon(icon_path))


window = MainWindow()
window.show()

sys.exit(app.exec())
