#   Importing libraries

import typing # Lambda Functions
import wpilib 
import constants # Constant variables from constants.py
import commands2
from commands2 import button 

from subsystems.climber import Climber
from commands.activate_climber import ExtendClimber, ContractClimber
# Importing Drivetrain subsystem
from subsystems.drivetrain import Drivetrain
from commands.defaultdrivetrain import DefaultDrivetrain

# In this class, has created Drivetrain controls system
class RobotContainer:
    def __init__(self) -> None:
        self.robot_drive = Drivetrain() #Creating function
        self.climber = Climber()
        self.joystick = wpilib.Joystick(constants.C_DRIVER_CONTROLLER) # Identifying
        self.robot_drive.setDefaultCommand(
            DefaultDrivetrain(
                self.robot_drive, 
                lambda: self.joystick.getRawAxis(1) * constants.C_BUFFER_X_SPEED,
                lambda: self.joystick.getRawAxis(0) * constants.C_BUFFER_Z_ROTATION,
            )
        )

      
    def configureButtonBindings(self):
        commands2.button.POVButton(self.joystick, 0).whenHeld(
            ExtendClimber(self.climber)
        )

        commands2.button.POVButton(self.joystick, 180).whenHeld(
            ContractClimber(self.climber)
        )

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected() 