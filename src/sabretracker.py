import requests
import base64
import time
import RPi.GPIO as GPIO

from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=19, pin_rw=None, pin_e=16, pins_data=[21,18,23,24], numbering_mode=GPIO.BOARD, cols=16, rows=2, dotsize=8)

while True:
  lcd.write_string('Sabretracker')
  lcd.crlf()
  lcd.write_string('Sabretracker')
  time.sleep(5)