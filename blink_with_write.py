import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

ITER_COUNT = 15
DEBUG = False

if '-debug' in sys.argv:
   DEBUG = True

LED_PIN = 11
LED_IS_ON = False

GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)

SWITCH_PIN =37; 

GPIO.setup(SWITCH_PIN, GPIO.IN)


# Only execute if swtich is on

with open('data.txt', 'w') as data:

   for i in range(0, ITER_COUNT):

      # When switch is on, the LED light alternates.
      if(GPIO.input(SWITCH_PIN)):
      
         GPIO.output(LED_PIN, LED_IS_ON)
         data.write(f'{time.time():1.0f}     {LED_IS_ON}\n')
         if DEBUG:
            print(f'LED is on: {LED_IS_ON}\n')
         LED_IS_ON = not(LED_IS_ON)
         time.sleep(1)
         
      #When switch is off, the LED is always OFF. 
      else:
         if DEBUG:
            print("The switch is OFF.")
         LED_IS_ON = False
         GPIO.output(LED_PIN, LED_IS_ON)
         data.write(f'{time.time():1.0f}     {LED_IS_ON}\n')
         time.sleep(1)    

   
GPIO.cleanup()
