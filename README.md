# PRIVATE EXAM BROWSER

"Private Exam Browser" is a simple yet customizable web browser application built using PyQt5 and PyQtWebEngine. This browser can be used to prevent students from opening other programs on their machines. This program has the following features:
- Custom User-Agent: The User-Agent string used by the browser can be customized in the set_custom_user_agent function. This feature can help check if the student is accessing your website/app using this browser or not.
- Prevent Window Switching: The application prevents switching to other windows while the active window is not the "PRIVATE BROWSER" window.
- Window Stay-on-Top: The browser window stays on top of other windows, preventing them from obscuring the browser.
- Close Button: Users can close the application by clicking the "EXIT" button.
- User IP: When a user opens and closes the app, it sends a request to `WEBHOOK_URL` (this can be changed to your backend) to track how many users are online.
- Authentication: User will need to login with their user name and password, this can also help to check which user is online and taken the test

## Installation
Install PyQt5 and PyQtWebEngine

You can install PyQt5 and PyQtWebEngine using the Python package manager, pip. Open your command prompt or terminal and enter the following commands:
```bash
pip install PyQt5
pip install PyQtWebEngine
pip install requests


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

### Notes
You can then compile the program into installable or standalone app using `PyInstaller` or similar module.

This project is licensed under the MIT License.

---

### Attribution Request

If you find this software useful in your project, we kindly request that you provide attribution by mentioning the original authors or project in your documentation, About page, or wherever appropriate. Attribution helps acknowledge the work of open-source contributors and encourages the sustainability of open-source software.

Example Attribution:
"Portions of this software are based on [Private Exam Browser](https://github.com/naonvl/private-exam-browser), which is licensed under the MIT License."

Thank you for your consideration!
