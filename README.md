# PRIVATE BROWSER

Private Browser is a simple web browser application built using PyQt5 and PyQtWebEngine. This browser can be use to prevent student from opening another programs on their machine. This program has these features :
- Custom User-Agent: The User-Agent string used by the browser can be customized in the `set_custom_user_agent`` function. This feature can help to check if the student access your website/app using this browser or not.
- Prevent Window Switching: The application prevents switching to other windows while the active window is not the "PRIVATE BROWSER" window.
- Window Stay-on-Top: The browser window stays on top of other windows, preventing them from obscuring the browser.
- Close Button: Users can close the application by clicking the "EXIT" button.

## Installation
Install PyQt5 and PyQtWebEngine

You can install PyQt5 and PyQtWebEngine using the Python package manager, pip. Open your command prompt or terminal and enter the following commands:
```bash
pip install PyQt5
pip install PyQtWebEngine

```
## Customization Options

### 1. User-Agent

You can customize the User-Agent string used by the browser by modifying the `set_custom_user_agent` function in `utils.py`. By default, it is set to `"NATEPBROWSER/1.0"`. You can change it to any desired User-Agent string.

```python
# utils.py

def set_custom_user_agent():
    custom_user_agent = "YOUR_USER_AGENT_STRING"
    profile = QWebEngineProfile.defaultProfile()
    profile.setHttpUserAgent(custom_user_agent)
```

### 3. Styling
The styling of buttons and input fields in the application can be customized by modifying the CSS styles in the main.py file. The default styles are provided to create a consistent look and feel. You can change the colors, fonts, and other CSS properties to match your preferred design.

```python
# main.py

# Example button styling
button_style = """
QPushButton {
    color: #FFFFFF;
    padding: 2px;
    font: 14px;
    padding: 3px 8px;
    border-radius: 10px;
}
QPushButton:hover {
    background: #bbbbbb;
}
"""
```
### 4. Removing URL Bar
You can remove the URL Bar and set the initial url inside main.py
```python
web_view.load(QUrl.fromUserInput("https://google.com")) # Change this URL

toolbar.addWidget(back_button)
toolbar.addWidget(forward_button)
toolbar.addWidget(reload_button)
toolbar.addWidget(url_input)  # This is the URL input field

toolbar.addWidget(back_button)
toolbar.addWidget(forward_button)
toolbar.addWidget(reload_button)
# toolbar.addWidget(url_input)  # Comment out or remove this line

```
### 5. Running the app
To run the application, execute the main.py script using Python:
```bash
python main.py
```