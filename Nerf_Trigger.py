print('program start')
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, Remote
from pybricks.parameters import Stop, Port, Color, Button
from pybricks.tools import wait, run_task, multitask

hub = PrimeHub(observe_channels=[198])
hub.speaker.volume(100)
#myRemote = Remote(name='Nintendo')


motorA = Motor(Port.A, reset_angle=True, profile=5) #with sticker
motorB = Motor(Port.B, reset_angle=True, profile=5)
speed = 1000
turn_angle = 180

def ready():
    while hub.ble.observe(198) == None:
        wait(10)

def launch_signal():

    print(hub.buttons.pressed())
    while hub.ble.observe(198) != True:
        wait(10)


def calibrate():

    start_targetA = -90 if motorA.angle() < 10 else 270
    start_targetB = -270 if motorB.angle() < -10 else 90

    motorA.run_target(speed, start_targetA, then=Stop.BRAKE, wait=False)
    motorB.run_target(speed, start_targetB, then=Stop.BRAKE, wait=True)




#main code
hub.light.on(Color.ORANGE)
calibrate()
ready()
hub.light.blink(Color.GREEN, (30, 1970))
launch_signal()
#fire
hub.light.blink(Color.RED, (100, 100))
motorA.run_angle(speed, -turn_angle, then=Stop.BRAKE, wait=False)
motorB.run_angle(speed, turn_angle, then=Stop.BRAKE, wait=True)
hub.speaker.beep(1000, 3000)
calibrate()


print('program end')