print('running')
#most of these imports are unnecessary
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
from usys import stdin
from uselect import poll

hub = PrimeHub()

leftM = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, reset_angle = True, profile = 15)
rightM = Motor(Port.E, positive_direction=Direction.CLOCKWISE, reset_angle = True, profile = 15)

red = Color(h = 0, s = 100, v = 100)
green = Color(h = 120, s = 100, v = 100)
speed = 250

keyboard = poll()
keyboard.register(stdin)

while True:
    key = stdin.read(1)
    if key == ' ':
        leftM.stop() #can change to .hold
        rightM.stop()
        hub.light.on(red)
    elif key == 'w':
        leftM.run(speed)
        rightM.run(speed)
        hub.light.on(green)
    elif key == 'a':
        leftM.run(-speed / 2)
        rightM.run(speed / 2)
    elif key == 'd':
        leftM.run(speed / 2)
        rightM.run(-speed / 2)
    elif key == 's':
        leftM.run(-speed)
        rightM.run(-speed)