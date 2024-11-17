print('program start')
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Stop, Port, Color, Button
from pybricks.tools import wait, run_task, multitask

hub = PrimeHub(observe_channels=[198])
#TODO read remote control

motorA = Motor(Port.A, reset_angle=True, profile=5) #with sticker
motorB = Motor(Port.B, reset_angle=True, profile=5)
print(motorB.angle())
speed = 200
turn_angle = 180


def launch_signal():
    while not Button.BLUETOOTH in hub.buttons.pressed():
        wait(10)

def calibrate():

    start_targetA = -90 if motorA.angle() < 10 else 270
    start_targetB = -270 if motorB.angle() < -10 else 90

    motorA.run_target(speed, start_targetA, then=Stop.BRAKE, wait=False)
    motorB.run_target(speed, start_targetB, then=Stop.BRAKE, wait=True)



calibrate()
launch_signal()
#fire
motorA.run_angle(speed, -turn_angle, then=Stop.BRAKE, wait=False)
motorB.run_angle(speed, turn_angle, then=Stop.BRAKE, wait=True)
wait(2000)
calibrate()


print('program end')