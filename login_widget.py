from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QFont
import requests

class LoginWidget(QDialog):
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url
        self.setWindowTitle("Login")
        self.setFixedSize(300, 150)

        self.username_label = QLabel("Username:")
        self.password_label = QLabel("Password:")
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Login")        
        self.login_button.setFont(QFont("Roboto", 12))
        self.login_button.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; }")
        self.login_button.clicked.connect(self.login) 
        self.apply_styles()

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)
    def apply_styles(self):
        input_style = """
        QLineEdit {
            border: 1px solid #ccc;
            border-radius: 14px;
            height: 30px;
            padding: 4px; 
            font-size: 14px;
        }
        """
        self.username_input.setStyleSheet(input_style)
        self.password_input.setStyleSheet(input_style)
        button_style = """
        QPushButton {
            color: white;
            background-color: #4CAF50; 
            border-radius: 20px;
            padding: 5px 10px; 
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #45A049; /* Change color on hover */
        }
        """
        self.login_button.setStyleSheet(button_style)
        self.password_input.setEchoMode(QLineEdit.Password)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "admin" and password == "admin":
            user_ip = self.get_user_ip()
            self.send_app_opened_event(username, user_ip)
            self.accept() 
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def get_user_ip(self):
        try:
            response = requests.get('https://ipinfo.io')
            data = response.json()
            return data.get('ip')
        except Exception as e:
            print(f"Error fetching IP address: {e}")
            return None

    def send_app_opened_event(self, username, user_ip):
        if user_ip:
            # Send the app_opened event with username and user_ip
            payload = {"event": "app_opened", "username": username, "user_ip": user_ip}
            response = requests.get(self.webhook_url, params=payload)
            if response.status_code == 200:
                print("App opened event sent successfully.")
            else:
                print(f"Failed to send app_opened event: {response.status_code}")
        else:
            print("Unable to retrieve user's IP address.")
