#   Importing libraries

import typing # Lambda Functions
import wpilib 
import constants # Constant variables from constants.py

# Importing Drivetrain subsystem
from subsystems.drivetrain import Drivetrain
from commands.defaultdrivetrain import DefaultDrivetrain

# In this class, has created Drivetrain controls system
class RobotContainer:
    def __init__(self) -> None:
        self.robot_drive = Drivetrain() #Creating function

        self.joystick = wpilib.Joystick(constants.C_DRIVER_CONTROLLER) # Identifying
        self.robot_drive.setDefaultCommand(
            DefaultDrivetrain(
                self.robot_drive, 
                lambda: self.joystick.getRawAxis(1) * constants.C_BUFFER_X_SPEED,
                lambda: self.joystick.getRawAxis(0) * constants.C_BUFFER_Z_ROTATION,
            )
        )
