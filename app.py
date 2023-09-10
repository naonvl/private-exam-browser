import sys
from PyQt5.QtCore import QUrl, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
import pygetwindow as gw
import win32gui
import win32con
def set_custom_user_agent():
    custom_user_agent = "NATEPBROWSER/1.0"
    profile = QWebEngineProfile.defaultProfile()
    profile.setHttpUserAgent(custom_user_agent)
def prevent_window_switching():
    active_window = gw.getActiveWindow()

    if active_window is None or not active_window.title:
        return

    if active_window.title != "PRIVATE BROWSER":
        main_window.showFullScreen()
        active_window.minimize()

    timer.start(100)


def load_url():
    url = url_input.text()
    web_view.load(QUrl.fromUserInput(url))

app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle("PRIVATE BROWSER")
set_custom_user_agent()
main_window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

web_view = QWebEngineView()
web_view.load(QUrl.fromUserInput("https://google.com")) 

url_input = QLineEdit()
url_input.setPlaceholderText("Enter URL here")
url_input.setText("https://google.com") 
url_input.returnPressed.connect(load_url)

back_button = QPushButton(QIcon("back-icon.png"), "")
back_button.clicked.connect(web_view.back)

forward_button = QPushButton(QIcon("forward-icon.png"), "")
forward_button.clicked.connect(web_view.forward)

reload_button = QPushButton(QIcon("reload-icon.png"), "")
reload_button.clicked.connect(web_view.reload)

toolbar = QToolBar()
toolbar.addWidget(back_button)
toolbar.addWidget(forward_button)
toolbar.addWidget(reload_button)
toolbar.addWidget(url_input)
toolbar.setStyleSheet(""" 
    QToolBar {
        padding: 5px;  /* Added padding for the whole toolbar */
        background-color: #f1f1f1;  /* Set background color for the toolbar */
    }
""")
layout = QVBoxLayout()
layout.setContentsMargins(0, 5, 0, 0)
layout.addWidget(toolbar)
layout.addWidget(web_view)

central_widget = QWidget()
central_widget.setLayout(layout)

main_window.setCentralWidget(central_widget)

url_input.setStyleSheet("""
    QLineEdit {
        border: 1px solid #ccc;
        border-radius: 14px;
        padding: 5px;
        font-size: 14px;
    }
    QPushButton {
        border: 1px solid #ccc;
        border-radius: 20px;
        padding: 5px;
        font-size: 14px;
        background-color: #f1f1f1;
    }
    QPushButton:hover {
        background-color: #e1e1e1;
    }
""")
back_button.setStyleSheet(""" 
QPushButton {
    color: #FFFFFF;
    padding: 2px;
    font: 14px;
    padding:3px 8px;
    border-radius: 10px;
}
QPushButton:hover {
    background: #bbbbbb;
}
""")
forward_button.setStyleSheet(""" 
QPushButton {
    color: #FFFFFF;
    padding: 2px;
    font: 14px;
    padding:3px 8px;
    border-radius: 10px;
}
QPushButton:hover {
    background: #bbbbbb;
}
""")
reload_button.setStyleSheet(""" 
QPushButton {
    color: #FFFFFF;
    padding: 2px;
    font: 14px;
    padding:3px 8px;
    border-radius: 10px;
}
QPushButton:hover {
    background: #bbbbbb;
}
""")
timer = QTimer()
timer.timeout.connect(prevent_window_switching)
timer.start(100)
main_window.showFullScreen()
sys.exit(app.exec_())
