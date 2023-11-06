"""yaw_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, Supervisor, Node
import math

# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

YAW_ANGLE = 20
PITCH_ANGLE = 30


cone = supervisor.getFromDef("GAZE_TRACKER")
cone.enableContactPointsTracking(timestep)



p_motor = robot.getDevice('pitch_gaze')
y_motor = robot.getDevice('yaw_gaze')

while robot.step(timestep) != -1:

    p_motor.setPosition(math.radians(PITCH_ANGLE))
    y_motor.setPosition(math.radians(YAW_ANGLE))

    pass

# Enter here exit cleanup code.
