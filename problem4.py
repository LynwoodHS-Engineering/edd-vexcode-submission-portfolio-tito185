#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
distance_1 = Distance(Ports.PORT1)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
brain.screen.set_pen_color(Color.BLUE)
brain.screen.set_fill_color(Color.RED)
brain.screen.set_cursor(10,10)
x = distance_1.object_distance(MM)
while True:
 if x <= 250:
  brain.screen.set_pen_color(Color.BLUE)
  brain.screen.set_fill_color(Color.RED)
  brain.screen.set_cursor(10,10)
  x = distance_1.object_distance(MM)
  brain.screen.print(x)
  wait(0.1,SECONDS)
  brain.screen.clear_screen()
  brain.screen.set_cursor(10,10)
  brain.screen.draw_rectangle(0, 0, x, 50)
 else:
  brain.screen.set_pen_color(Color.RED)
  brain.screen.set_fill_color(Color.BLUE)
  brain.screen.set_cursor(10,10)
  x = distance_1.object_distance(MM)
  brain.screen.print(x)
  wait(0.1,SECONDS)
  brain.screen.clear_screen()
  brain.screen.set_cursor(10,10)
  brain.screen.draw_rectangle(0, 0, x, 50)
