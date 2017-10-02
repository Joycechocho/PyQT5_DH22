import sys
import time
import datetime
import Adafruit_DHT
from time import gmtime, strftime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        
        self.setWindowTitle('DHT22 Sensor Value')

        self.setToolTip('Click to request new data')

        self.label = QLabel('Temperature is {0:0.1f} Celsius Degree'.format(temperature), self)
        self.humid = QLabel('Humidity is '+str(round(humidity,2))+' %', self)
        self.lbled = QLabel(strftime("%Y-%m-%d %H:%M:%S", gmtime()), self)

        self.setFixedSize(500,500)
        #self.label.setAlignment(Qt.AlignCenter)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.humid, 1, 0)
        self.layout.addWidget(self.lbled, 2, 0)
        
        req_btn = QPushButton('Request', self)
        req_btn.clicked.connect(self.on_click)
        req_btn.setToolTip('Click to request new data')
        
        exit_btn = QPushButton('Quit', self)
        exit_btn.clicked.connect(QCoreApplication.instance().quit)
        exit_btn.move(100, 0)
        
        self.setLayout(self.layout)
        self.show()
        
            
    def on_click(self):
        if humidity is not None and temperature is not None:
            self.label.setText('Temperature is {0:0.1f} Celsius Degree'.format(temperature))
            self.humid.setText('Humidity is '+str(round(humidity,2))+' %')
        else:
            self.label.setText("Failed to read temperature data. Try again!")
            self.humid.setText("Failed to read humidity data. Try again!")
            print("fail")
        self.lbled.setText(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
      
 


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
