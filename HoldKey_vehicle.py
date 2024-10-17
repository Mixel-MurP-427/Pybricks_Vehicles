print('running')
#battlebot v2
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task

from usys import stdin
from uselect import poll

hub = PrimeHub()
hub.speaker.volume(100)

left = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, reset_angle = True, profile = 15)
right = Motor(Port.F, positive_direction=Direction.CLOCKWISE, reset_angle = True, profile = 15)
claw = Motor(Port.D, positive_direction=Direction.CLOCKWISE, reset_angle = True, profile = 5)
#sensor = ColorSensor(Port.A)

keyboard = poll()
keyboard.register(stdin)
past_keys = [None] * 20 #int is adjustable
key = None

def all_none(key_list):
    for item in range(len(key_list)):
        if not key_list[item] == None:
            return False
    return True

async def main():
    should_stop = 'yes'
    while True:
        await wait(10)
        if keyboard.poll(0): #reads key, if any.
            key = stdin.read(1)
            past_keys.append(key)
        else:
            past_keys.append(None)
        past_keys.pop(0)

        if all_none(past_keys) == False: #Checks if a key was recently pressed.
            should_stop = 'yes'
            if key == 'i' and 'i' in past_keys:
#                hub.speaker.beep(frequency = 500, duration = 1)
                claw.run_target(99999, 90, then = Stop.HOLD)
            elif key == 'k' and 'k' in past_keys:
                claw.run_target(-99999, -18, then = Stop.COAST)
            if key == ' ':
                left.hold()
                right.hold()
            elif 'w' in past_keys:
                left.run(99999)
                right.run(99999)
            elif 's' in past_keys:
                left.run(-99999)
                right.run(-99999)
            elif 'a' in past_keys:
                right.run(400)
                left.run(-400)
            elif 'd' in past_keys:
                left.run(400)
                right.run(-400)
            else:
                left.hold()
                right.hold()
        else:
            if should_stop == 'yes':
                left.stop()
                right.stop()
                should_stop = 'no'
            if left.speed() == 0 and right.speed() == 0:#test what happens without this block.
                left.hold()
                right.hold()

hub.system.set_stop_button(Button.BLUETOOTH)
hub.light.on(Color.RED)
run_task(main())