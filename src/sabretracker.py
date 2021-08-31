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

    if newdata[0:6] == "$GPRMC":
      newmsg=pynmea2.parse(newdata)
      lat=newmsg.latitude
      lng=newmsg.longitude
      gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
      print(gps)

      lcd.clear()
      lcd.write_string(f'Lat={str(lat)}'[:16])
      lcd.cursor_pos=(1,0)
      lcd.write_string(f'Lng={str(lng)}'[:16])

    if newdata[0:6] == "$GPVTG":
      msg = newdata.split(',')
      speed = msg[7]
      print(speed)
      lcd.clear()
      lcd.write_string(f"{speed} km/h")
      time.sleep(0.5)
    
    if newdata.startswith("$GPVTG") :
      data = pynmea2.parse(newdata)
      gpsSpeedText = "Speed: {speed} Kmh".format(speed=data.spd_over_grnd_kmph)
    if newdata.startswith("$GPRMC") :
      data = pynmea2.parse(newdata)
      gpsSpeedText2 = "Speed: {speed} Kmh".format(speed=data.spd_over_grnd)
  
  except Exception as e:
    print(f'ops with error={e}')
