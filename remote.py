#A remote that broadcasts its pitch and roll tilt angles

print('running')
from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis

hub = MoveHub(top_side = Axis.Z, front_side = Axis.Y, broadcast_channel = 128) #128 is an arbitrary channel
hub.light.on(Color.GREEN)

while True:
    pitch, roll = hub.imu.tilt()
#    print(str(pitch) + ' ' + str(roll))
    hub.ble.broadcast([True, pitch, roll]) #True indicates that it is broadcasting its gyro angles and not the joystick positions (a feature I may later add)