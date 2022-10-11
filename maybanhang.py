from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("Xin Chao!", 1)
    lcd.text("Moi Ban Quet The", 2)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()    

