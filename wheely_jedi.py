#this is currently a prototype meant to run in Pybricks
#
#   THIS IS MY VERSION OF THE PROGRAM.  
#   I CHANGED ALMOST NOTHING EXCEPT FOR 
#   THE IMPORT STATEMENTS.
#
#
print('running')
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.tools import wait as somethingtodo
from pybricks.tools import run_task

#initialization
hub = PrimeHub(top_side = Axis.Z, front_side = Axis.Y, observe_channels = [128])
hub.system.set_stop_button(Button.BLUETOOTH)
hub.display.orientation(Side.LEFT)
hub.speaker.volume(75)
#max motor speed is 1050ish
motorL = Motor(port = Port.B, positive_direction = Direction.COUNTERCLOCKWISE, profile = 20)
motorR = Motor(port = Port.E, positive_direction = Direction.CLOCKWISE, profile = 20)
cap_speed = 1050 #constant
max_speed = 100 #maximum speed motors is allowed to reach. Can be adjusted during play.
min_speed = 100
screen_speed = 1 #ranges from 1 to 25
speed_interval = (cap_speed - min_speed) / 25
arrow_clock = 0
speedL = 0 #speeds for motors
speedR = 0
high_speed = 0 #used in basic_drive() to find highest speed indicated by remote
other_speed = 0
pitchRC_Y = 0 #tilt angles given by RC
rollRC_X = 0
max_RC_output = 60 #constant that determines how far the RC is allowed to be tilted


#Determines motor speed mapping
def basic_drive():
    global pitchRC_Y, rollRC_X, speedL, speedR, high_speed, other_speed
    #set max remote output
    if pitchRC_Y > max_RC_output:
        pitchRC_Y = max_RC_output
    elif pitchRC_Y < -max_RC_output:
        pitchRC_Y = -max_RC_output
    if rollRC_X > max_RC_output:
        rollRC_X = max_RC_output
    elif rollRC_X < -max_RC_output:
        rollRC_X = -max_RC_output
    #find the top speed given by the remote
    if abs(rollRC_X) > abs(pitchRC_Y):
        high_speed = abs(rollRC_X)
    else:
        high_speed = abs(pitchRC_Y)
    #find other indicated speed for other motor
    other_speed = abs(rollRC_X) - abs(pitchRC_Y)
    #determine motor speeds. Negatives are needed for certain cases, depending on the quadrant.
    if rollRC_X > 0: #if tilted right
        if pitchRC_Y < 0: #if tilted down
            speedR = -high_speed
            speedL = other_speed
        else: #tilted up
            speedL = high_speed
            speedR = -other_speed
        
    else:# rollRC_X < 0: #tilted left
        if pitchRC_Y < 0: #if tilted down
            speedL = -high_speed
            speedR = other_speed
        else: #tilted up
            speedR = high_speed
            speedL = -other_speed

def right_arrow():
    if Button.RIGHT in hub.buttons.pressed() and len(hub.buttons.pressed()) == 1:
        return True
    else:
        return False

def left_arrow():
    if Button.LEFT in hub.buttons.pressed() and len(hub.buttons.pressed()) == 1:
        return True
    else:
        return False

#
async def speed_buttons():
    global cap_speed, max_speed, min_speed, screen_speed, speed_interval, arrow_clock
    hub.light.off()
    arrow_clock = 0
    while arrow_clock < 2000:
        if right_arrow() and not screen_speed == 25:
            screen_speed += 1
            max_speed += speed_interval
            arrow_clock = 0
            await hub.speaker.beep(frequency = 500, duration = 50)
            awaitsomethingtodo(100)
        if left_arrow() and not screen_speed == 1:
            screen_speed -= 1
            max_speed -= speed_interval
            arrow_clock = 0
            await hub.speaker.beep(frequency = 500, duration = 50)
            awaitsomethingtodo(100)
        #hub.display.icon([100] * screen_speed + [0] * (25 - screen_speed))
        awaitsomethingtodo(100)
        arrow_clock += 100


async def main():
    global motorL, motorR, cap_speed, max_speed, min_speed, screen_speed, speed_interval, arrow_clock, speedL, speedR, high_speed, other_speed, pitchRC_Y, rollRC_X, max_RC_output
    while True:
        await somethingtodo(100) #see directory example for explanation. Test if await keyword is needed.
        infoRC = hub.ble.observe(128)#gets output from RC
        if infoRC == None:
            hub.light.on(Color.RED)
            pitchRC_Y = 0
            rollRC_X = 0
        else:
            hub.light.on(Color.GREEN)
            pitchRC_Y = infoRC[1] #forward/backward RC tilt
            rollRC_X = infoRC[2] #left/right RC tilt

        if left_arrow() or right_arrow():
            run_task(speed_buttons())
            #return screen to arrow animation at end of speed_buttons()

        basic_drive()
        motorL.run(speedL * (max_speed / max_RC_output))
        motorR.run(speedR * (max_speed / max_RC_output))


run_task(main())