import time
import serial              
import sys
import RPi.GPIO as GPIO
import pynmea2

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)
ser=serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.5)

while True:
  try:
    dataout = pynmea2.NMEAStreamReader()
    newdata = (str)(ser.readline())
    newdata.decode('utf-8')

    if newdata[0:6] == "$GPRMC":
      print('entrou')
      newmsg=pynmea2.parse(newdata)
      lat=newmsg.latitude
      lng=newmsg.longitude
      gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
      print(gps)

    #received_data = (str)(ser.readline()) #read NMEA string received
    #print(received_data, "\n")
  except Exception as e:
    print(e)
