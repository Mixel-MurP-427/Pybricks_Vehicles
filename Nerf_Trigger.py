print('program start')
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Stop, Port, Color, Button
from pybricks.tools import wait, run_task, multitask

hub = PrimeHub(observe_channels=[198])
#TODO read remote control

motorA = Motor(Port.A) #with sticker
motorB = Motor(Port.B)
motorA.reset_angle()
motorB.reset_angle()

async def launch_signal():
    while not Button.BLUETOOTH in hub.buttons.pressed():
        await wait(10)

async def main():



    

    #startup
    motorA.run_target(200, -90, then=Stop.COAST, wait=False)
    motorB.run_target(200, 90, then=Stop.COAST, wait=True)

    await launch_signal()
    print('pressed')

    motorA.run_target(200, -180, then=Stop.COAST, wait=False)
    motorB.run_target(200, 180, then=Stop.COAST, wait=True)
    await wait(2000)


run_task(main())
print('program end')