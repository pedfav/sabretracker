import time
import serial              
import sys
import RPi.GPIO as gpio
import pynmea2
import uuid

from RPLCD.gpio import CharLCD

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=gpio.BOARD, cols=16, rows=2, dotsize=8)
gpio.setup(15, gpio.IN, pull_up_down = gpio.PUD_DOWN)

def print_to_lcd(first_line, second_line):
  lcd.clear()
  lcd.write_string(first_line)
  lcd.cursor_pos=(1,0)
  lcd.write_string(second_line)

while True:
  try:
    ser=serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)
    #dataout = pynmea2.NMEAStreamReader()
    newdata=ser.readline()
    newdata=newdata.decode('utf-8')
    #print(gps)

    if newdata.startswith("$GPRMC"):
      newmsg=pynmea2.parse(newdata)
      lat=newmsg.latitude
      lng=newmsg.longitude
      gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
      print(gps)

      if(gpio.input(15) == 1):
        print_to_lcd(f'Lat={str(lat)}'[:16], f'Lng={str(lng)}'[:16])

    gpsSpeedText = ''
    gpsSpeedText2 = ''
    if newdata.startswith("$GPVTG") :
      print('clid')
      data = pynmea2.parse(newdata)
      gpsSpeedText = "GPVTG: {speed} Kmh".format(speed=data.spd_over_grnd_kmph)
      print(gpsSpeedText)
    if newdata.startswith("$GPRMC") :
      data = pynmea2.parse(newdata)
      gpsSpeedText2 = "GPRMC: {speed} Kmh".format(speed=data.spd_over_grnd)
      print(gpsSpeedText2)
    
    if(gpio.input(15) == 0):
      print_to_lcd(gpsSpeedText, gpsSpeedText2)

  except Exception as e:
    print(f'ops with error={e}')
