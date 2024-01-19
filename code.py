import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("LED On")
while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
    
