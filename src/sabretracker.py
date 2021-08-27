import time
import serial              
import sys
import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)
ser = serial.Serial ("/dev/serial0", 9600)

while True:
  try:
    received_data = (str)(ser.readline()) #read NMEA string received
    print(received_data, "\n")
    lcd.write_string('Sabretracker')
    lcd.crlf()
    lcd.write_string('Sabretracker')
    print('print lcd')
    time.sleep(5)
  except Exception as e:
    print(e)