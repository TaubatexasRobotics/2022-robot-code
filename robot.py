import wpilib
import commands2

# From here, start the robot commands by RobotContainer
from robotcontainer import RobotContainer

class TaubatexasRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()

# Defines robot.py as main module and start robot code
if __name__ == '__main__':
    wpilib.run(TaubatexasRobot)
