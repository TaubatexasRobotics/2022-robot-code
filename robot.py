'''
This program demonstrates the complete operation, importing libraries and starting classes.
Our robot it contains the code necessary to operate a robot with
a single joystick
'''

import wpilib
import commands2

# From here, start the robot commands by RobotContainer

from robotcontainer import RobotContainer

class TaubatexasRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()

# Start TaubatexasRobot Class

if __name__ == '__main__':
    wpilib.run(TaubatexasRobot) 
