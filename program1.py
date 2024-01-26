import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering


pin1 = 11 #Pin for providng power
pin2 = 37 #Pin for detecting switch state


GPIO.setup(pin2, GPIO.IN)
GPIO.setup(pin1, GPIO.OUT, initial = GPIO.LOW)


#Check the state of the switch
while(True):
   if GPIO.input(pin2):
      GPIO.output(pin1, GPIO.HIGH)
   else:
      GPIO.output(pin1, GPIO.LOW)
 

GPIO.cleanup()
