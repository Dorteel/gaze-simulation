"""yaw_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, Supervisor, Node
import math

# create the Robot instance.
supervisor = Supervisor()

# get the time step of the current world.
timestep = int(supervisor.getBasicTimeStep())

YAW_ANGLE = 20
PITCH_ANGLE = 30


cone = supervisor.getFromDef("gaze_tracker")
cone.enableContactPointsTracking(timestep)



p_motor = supervisor.getDevice('pitch_gaze')
y_motor = supervisor.getDevice('yaw_gaze')

while supervisor.step(timestep) != -1:

    p_motor.setPosition(math.radians(PITCH_ANGLE))
    y_motor.setPosition(math.radians(YAW_ANGLE))

    pass

# Enter here exit cleanup code.
