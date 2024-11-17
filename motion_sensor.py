print('program start')
from pybricks.hubs import MoveHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

hub = MoveHub(broadcast_channel=198)
sensor = UltrasonicSensor(Port.C)
margin = 20 #allowance for triggering

hub.light.blink(Color.BLUE, (500, 500))
sensor.lights.on(100)
wait(5000)


hub.light.on(Color.ORANGE)

#get average distance once resting
distances = []
for _ in range(100):
    wait(100)
    distances.append(sensor.distance())
    if distances[-1] == 2000: #does not accept 2000 as a distance
        del distances[-1]

#process
counter = 0
for dist in distances: counter += dist
mean_dist = counter // len(distances)
print(mean_dist, len(distances))

#begin sensing

hub.light.blink(Color.GREEN, (30, 1970))
sensor.lights.off()
hub.ble.broadcast(False)
current_dist = sensor.distance()
while (current_dist < mean_dist+margin or current_dist==2000) and current_dist > mean_dist-margin: #does not accept 2000 as a distance
    current_dist = sensor.distance()
    wait(50)

#fire
print(current_dist)
hub.ble.broadcast(True)
hub.light.blink(Color.RED, (100, 100))
sensor.lights.on(100)
wait(5000)
print('program end')