import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout

from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter city name",self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Get weather",self)
        self.temperature_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("WeatherApp")

        vbox = QVBoxLayout()

        # Add widgets to the layout
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)  # Add the input field
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        # Apply the layout to the main widget
        self.setLayout(vbox)

        # Align widgets
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.get_weather_button.setStyleSheet("margin: 0 auto;")  # Center button via CSS if needed
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        #CSS styling{ }

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        #Styling the widgets
        self.setStyleSheet("""
        QLabel,QPushButton{
        font-family: calibri;}

        QLabel#city_label{
        font-size:40px;
        font-style:italic;
        }

        QLineEdit#city_input{
         font-size:40px;

        }
        QPushButton#get_weather_button{
        font-size:30px;
        font-weight:bold;
        }
        QLabel#temperature_label{
        font-size: 75px;}

        QLabel#emoji_label{
        font-size:100px;
        font-family: Segoe UI emoji;}

        QLabel#description_label{
        font-size:50px;}
        
        """)

        self.get_weather_button.clicked.connect(self.getWeather)

    def getWeather(self):
        api_key = "d65c964819c94251a9b163331252104"  # Replace with your actual API key
        city = self.city_input.text()
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Correct typo
            data = response.json()

            if "error" in data:  # Check for errors in the API response
                self.display_error(data["error"]["message"])
            else:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_err:
            self.display_error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            self.display_error(f"Request error occurred: {req_err}")


    def display_error(self, message):
        pass

    def display_weather(self,data):
        temperture_c= data["current"]["temp_c"]
        print(f"{temperture_c}°C")
        weather_description = data["current"]["condition"]["text"]
        

        self.temperature_label.setText(f"{temperture_c:.0f}°C")
        self.description_label.setText( weather_description)
    

    @staticmethod
    def get_weather_button(weather_id):
        pass



if __name__=="__main__":
    app =  QApplication(sys.argv)
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())