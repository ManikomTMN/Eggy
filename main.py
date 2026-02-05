import sys, os, ctypes, time
import platform
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QIcon, QGuiApplication, Qt, QPixmap
from app.main_window import MainWindow

app = QApplication(sys.argv)

def resource_path(relative_path):
    try:
        # PYINStaller creats this _meipass thingo.
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Dark Mode
QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Dark)

app.setWindowIcon(QIcon(resource_path("ICON.ico")))

myappid = 'manikomtmn.eggy.whatever'

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

splash_pix = QPixmap("splash.png")
splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
splash.show()

app.processEvents()
time.sleep(1)

window = MainWindow()
window.show()

splash.finish(window)

sys.exit(app.exec())

