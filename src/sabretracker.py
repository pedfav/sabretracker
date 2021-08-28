import time
import serial              
import sys
import RPi.GPIO as GPIO
import pynmea2

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)
#ser=serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)

while True:
  try:
    lcd.clear()
    lcd.write_string('H4CK3r')
    lcd.cursor_pos=(1,0)
    lcd.write_string('c0ck 5uck3r')

    #received_data = ser.readline() #read NMEA string received
    #print(received_data, "\n")
  except Exception as e:
    print(e)
