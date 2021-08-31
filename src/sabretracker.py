import time
import serial              
import sys
import RPi.GPIO as GPIO
import pynmea2
import uuid

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

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

      lcd.clear()
      lcd.write_string(f'Lat={str(lat)}'[:16])
      lcd.cursor_pos=(1,0)
      lcd.write_string(f'Lng={str(lng)}'[:16])
      time.sleep(0.5)

    gpsSpeedText = ''
    gpsSpeedText2 = ''
    if newdata.startswith("$GPVTG") :
      data = pynmea2.parse(newdata)
      gpsSpeedText = "Speed GPVTG: {speed} Kmh".format(speed=data.spd_over_grnd_kmph)
      print(gpsSpeedText)
    if newdata.startswith("$GPRMC") :
      data = pynmea2.parse(newdata)
      gpsSpeedText2 = "Speed GPRMC: {speed} Kmh".format(speed=data.spd_over_grnd)
      print(gpsSpeedText2)
    
    lcd.clear()
    lcd.write_string(gpsSpeedText)
    lcd.cursor_pos=(1,0)
    lcd.write_string(gpsSpeedText2)
    time.sleep(0.5)

  except Exception as e:
    print(f'ops with error={e}')
