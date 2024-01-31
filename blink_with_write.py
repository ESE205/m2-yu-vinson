import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

start_time = time.time()

DEBUG = False

if '-debug' in sys.argv:
   DEBUG = True

blink_rate = input("Please enter the blink rate: ")
try:
   blink_rate = float(blink_rate)
except ValueError:
   blink_rate = 1

duration = input("Please enter the total running time of program: ")

try:
   duration = float(duration)
except ValueError:
   duration = 15 #Default time is 15 seconds

LED_PIN = 11
LED_IS_ON = False

GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)

SWITCH_PIN =37

GPIO.setup(SWITCH_PIN, GPIO.IN)


# Only execute if swtich is on

with open('data.txt', 'w') as data:

   while True:
      # Stop the program when time ends
      stop_time = time.time() - start_time
      if stop_time >= duration:
          break
    
      # When switch is on, the LED light alternates.
      if(GPIO.input(SWITCH_PIN)):

         GPIO.output(LED_PIN, LED_IS_ON)
         data.write(f'{time.time():1.0f}     {LED_IS_ON}\n')
         if DEBUG:
            print(f'LED is on: {LED_IS_ON}\n')
         LED_IS_ON = not(LED_IS_ON)
         time.sleep(blink_rate)

      #When switch is off, the LED is always OFF.
      else:
         if DEBUG:
            print("The switch is OFF.")
            LED_IS_ON = False
            GPIO.output(LED_PIN, LED_IS_ON)
            data.write(f'{time.time():1.0f}     {LED_IS_ON}\n')
            time.sleep(blink_rate)


GPIO.cleanup()
