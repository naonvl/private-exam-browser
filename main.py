import sys
import requests
from PyQt5.QtCore import QUrl, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout, QToolBar, QDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pygetwindow as gw
from utils import set_custom_user_agent, prevent_window_switching, load_url
from login_widget import LoginWidget


WEBHOOK_URL = "https://webhook.site/8be380ee-8bb2-4df1-bbff-a26518ef2209"

def get_user_ip():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data.get('ip')
    except Exception as e:
        print(f"Error fetching IP address: {e}")
        return None


class MainWindow(QMainWindow):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F4 and (event.modifiers() & Qt.AltModifier):
            event.ignore()
        else:
            super().keyPressEvent(event)

def create_main_window():
    app = QApplication(sys.argv)
    login_widget = LoginWidget(WEBHOOK_URL)
    if login_widget.exec_() == QDialog.Accepted:
        main_window = QMainWindow()
        main_window.setWindowTitle("PRIVATE BROWSER")
        set_custom_user_agent()
        main_window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        web_view = QWebEngineView()
        web_view.load(QUrl.fromUserInput("https://google.com"))

        user_ip = get_user_ip()

        if user_ip:
            requests.get(WEBHOOK_URL, params={"event": "app_opened", "user_ip": user_ip})
        else:
            print("Unable to retrieve user's IP address.")

        def close_app():
            requests.get(WEBHOOK_URL, params={"event": "app_closed", "user_ip": user_ip})
            app.quit()

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

        close_button = QPushButton()
        close_button.setText("EXIT")
        close_button.clicked.connect(close_app)

        button_style = """
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
        """
        back_button.setStyleSheet(button_style)
        forward_button.setStyleSheet(button_style)
        reload_button.setStyleSheet(button_style)
        close_button.setStyleSheet(button_style)

        toolbar = QToolBar()
        toolbar.addWidget(back_button)
        toolbar.addWidget(forward_button)
        toolbar.addWidget(reload_button)
        toolbar.addWidget(url_input)
        toolbar.addWidget(close_button)
        toolbar.setStyleSheet("""
            QToolBar {
                padding: 5px;
                background-color: #f1f1f1;
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
        """)

        timer = QTimer()
        timer.timeout.connect(lambda: prevent_window_switching(main_window))
        timer.start(100)
        main_window.showFullScreen()
        sys.exit(app.exec_())

if __name__ == "__main__":
    create_main_window()
