import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.original_button_style = None
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.city_label = QLabel("...", self)
        self.city_temp = QLabel("...", self)
        self.weather_description = QLabel("...", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("weather.png"))
        self.setFixedSize(400, 450)

        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.city_label.setObjectName("city_label")
        self.city_temp.setObjectName("city_temp")
        self.weather_description.setObjectName("weather_description")

        self.city_input.setPlaceholderText("Enter a city")

        hbox = QHBoxLayout()
        hbox.addWidget(self.city_input)
        hbox.addWidget(self.get_weather_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_temp)
        vbox.addStretch()
        vbox.addWidget(self.weather_description)
        vbox.addStretch()
        self.setLayout(vbox)

        self.setStyleSheet("""
            QLabel{
                Font-family: Arial;
            }
            QLineEdit, QPushButton{
                font-family: arial;
                font-size: 16px;
                Padding: 8px;
                border: none;
                border-radius: 8px;
                margin: 0 4;
            }
            QPushButton{
                background-color: black;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: #4C5052;
            }
            QLabel#city_label{
                font-size: 36px;
            }
            QLabel#city_temp{
                font-size: 48px;
            }
            QLabel#weather_description{
                font-size: 24px;
            }
        """)

        self.original_button_style = """
            QPushButton{
                background-color: black;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: #4C5052;
            }
        """

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_temp.setAlignment(Qt.AlignCenter)
        self.weather_description.setAlignment(Qt.AlignCenter)

        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    def get_weather(self):

        self.get_weather_button.setStyleSheet("background-color: lightgrey;")
        # Use a QTimer to reset the color after a short delay (e.g., 200 milliseconds)
        QTimer.singleShot(200, self.reset_button_color)

        api_key = "a10f81bb93e345f12eb278c352a4cd4d"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        if not city:
            self.show_error("Please enter a city")
            return

        try:
            response = requests.get(url)
            data = response.json()

            if data['cod'] == 200:
                self.show_weather(data)
            else:
                self.show_error(data.get('message', "There was an error"))
        except requests.exceptions.RequestException as e:
            self.show_error(f"Network error: {e}")

    def reset_button_color(self):
        """Resets the button's background color to its original state."""
        self.get_weather_button.setStyleSheet(self.original_button_style)

    def show_error(self, message):
        self.city_label.setText("Error")
        self.city_temp.setText("...")
        self.weather_description.setText(message)

    def show_weather(self, data):
        temp_c = f"{data['main']['temp'] - 273.15:.1f}°C"

        self.city_label.setText(data['name'])
        self.city_temp.setText(temp_c)
        self.weather_description.setText(data['weather'][0]['description'])

        print(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
    