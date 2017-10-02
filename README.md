# Author
Joyce Cho 

# Description
This application is developed for Embedded Interface Design Project-1 at University of Colorado Boulder. When receiving the temperature and humidity data from DH22, the value can be shown on the window application. 

# Environment
Python-DHT Library from Adafruit Python DHT Sensor Library (https://github.com/adafruit/Adafruit_Python_DHT)

Python3

QT5

PyQT5

DH22 sensor

Raspberry pi3

4.7k resistor

# Features
1. Use a button to allow the request of current humidity/temperature values from the DHT22
2. Display the values as well as the time of the request
3. Handle not receiving data when requested

# Running
First, we need to install the library from https://github.com/adafruit/Adafruit_Python_DHT

After configuring the library ,  run the command as below
```
python3 sensorui.py 22 4
```
The first argument is to target the sensor. 22 = DH22 sensor

The second argement is to target the GPIO pin on raspberry pi. 4 = GPIO4

# Demo
![alt text](https://github.com/Joycechocho/PyQT5_DH22/blob/master/demo.png)

I created a "request" button to allow the request of current humidity/temperature values from the DHT22.

For each request, the time of the request would change base on the current time. 

When the sensor data is null, it would throw an error message. 
