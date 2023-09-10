import pygetwindow as gw
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

def set_custom_user_agent():
    custom_user_agent = "NATEPBROWSER/1.0"
    profile = QWebEngineProfile.defaultProfile()
    profile.setHttpUserAgent(custom_user_agent)

def prevent_window_switching(main_window):
    active_window = gw.getActiveWindow()

    if active_window is None or not active_window.title:
        return

    if active_window.title != "PRIVATE BROWSER":
        main_window.showFullScreen()
        active_window.minimize()

def load_url(main_window):
    url = main_window.url_input.text()
    main_window.web_view.load(QUrl.fromUserInput(url))
