"""yaw_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
import math

YAW_ANGLE = 20
PITCH_ANGLE = 30

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

p_motor = robot.getDevice('pitch_gaze')
y_motor = robot.getDevice('yaw_gaze')

while robot.step(timestep) != -1:

    p_motor.setPosition(math.radians(PITCH_ANGLE))
    y_motor.setPosition(math.radians(YAW_ANGLE))

    pass

# Enter here exit cleanup code.
