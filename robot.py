import wpilib
import commands2
#from serial import serial

# From here, start the robot commands by RobotContainer
from robot_container import RobotContainer

class TaubatexasRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()

    def teleopInit(self) -> None:
        self.container.configureButtonBindings()
    
    def autonomousPeriodic(self) -> None:
        self.container.intake.intake_pull()
        self.container.StopIntakeSwitch()

# Start TaubatexasRobot Class
if __name__ == '__main__':
    wpilib.run(TaubatexasRobot)