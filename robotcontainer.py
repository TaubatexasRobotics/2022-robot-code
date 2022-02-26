
# Importing libraries
import typing # Lambda Functions
import wpilib
from commands.intakeArm import IntakeDown, IntakeUp
from commands.intakeAtivarCommand import PullIntake, PushIntake 
import constants # Constant variables from constants.py
import commands2
from commands2 import button 

from subsystems.climber import Climber
from commands.activate_climber import ExtendClimber, ContractClimber

import commands2
import commands2.button

# Importing Drivetrain subsystem
from subsystems.drivetrain import Drivetrain
from commands.defaultdrivetrain import DefaultDrivetrain

from subsystems.shooter import Shooter
from commands.shootcommand import ShooterCommand

from subsystems.intakeArm import intakeArm
from subsystems.intakeAtivar import intakeActive

# In this class, has created Drivetrain controls system
class RobotContainer:
    def __init__(self) -> None:
        self.robot_drive = Drivetrain() #Creating function

        self.climber = Climber()

        self.intakeArm = intakeArm

        self.intakeActive = intakeActive

        self.joystick = wpilib.Joystick(constants.C_DRIVER_CONTROLLER) # Identifying
        
        self.robot_drive.setDefaultCommand(
            DefaultDrivetrain(
                self.robot_drive, 
                lambda: self.joystick.getRawAxis(1) * constants.C_BUFFER_X_SPEED,
                lambda: self.joystick.getRawAxis(0) * constants.C_BUFFER_Z_ROTATION,
            )
        )



    def configureButtonBindings(self):
        commands2.button.POVButton(self.joystick, 1).whenHeld(
            PullIntake(self.intakeArm)
        )

        commands2.button.POVButton(self.joystick, 2).whenHeld(
            PushIntake(self.intakeArm)
        )



    def configureButtonBindings(self):
        commands2.button.POVButton(self.joystick, 3).whenHeld(
            IntakeUp(self.intakeActive)
        )

        commands2.button.POVButton(self.joystick, 4).whenHeld(
            IntakeDown(self.intakeActive)
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
