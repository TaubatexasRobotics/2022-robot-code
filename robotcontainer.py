
# Importing libraries
#import typing # Lambda Functions
import wpilib

import constants # Constant variables from constants.py
import commands2

import commands2.button

from subsystems.climber import Climber
from commands.activate_climber import ExtendClimber, ContractClimber

# Importing Drivetrain subsystem
from subsystems.drivetrain import Drivetrain
from commands.defaultdrivetrain import DefaultDrivetrain

from subsystems.intakeArm import IntakeArm
#from subsystems.intakeAtivar import IntakeActive

from commands.intakeArmCmd import IntakeDownCmd, IntakeUpCmd
# from commands.intakeAtivarCommand import PullIntake, PushIntake 

# In this class, has created Drivetrain controls system
class RobotContainer:
    def __init__(self) -> None:
        self.robot_drive = Drivetrain() #Creating function
        self.climber = Climber()
        self.intakeArm = IntakeArm()
        #self.intakeActive = IntakeActive()
        self.joystick = wpilib.Joystick(constants.C_DRIVER_CONTROLLER) # Identifying
        
        self.robot_drive.setDefaultCommand(
            DefaultDrivetrain(
                self.robot_drive, 
                lambda: self.joystick.getRawAxis(1) * constants.C_BUFFER_X_SPEED,
                lambda: self.joystick.getRawAxis(0) * constants.C_BUFFER_Z_ROTATION,
            )
        )

    def configureButtonBindings(self):
        # INTAKE ACTIVE
        # commands2.button.JoystickButton(self.joystick, 1).whenHeld(
        #     PullIntake(self.intakeArm) #INTAKE ACTIVE
        # )

        # commands2.button.JoystickButton(self.joystick, 2).whenHeld(
        #     PushIntake(self.intakeArm) #INTAKE ACTIVE
        # )

        # INTAKE ARM
        # IntakeUp levanta o braço do intake
        commands2.button.JoystickButton(self.joystick, 3).whenHeld(
            IntakeUpCmd(self.intakeArm)
        )

        #IntakeDown abaixa o braço do intake
        commands2.button.JoystickButton(self.joystick, 4).whenHeld( 
            IntakeDownCmd(self.intakeArm)
        )

        # CLIMBER
        commands2.button.POVButton(self.joystick, 0).whenHeld(
            ExtendClimber(self.climber)
        )
        commands2.button.POVButton(self.joystick, 180).whenHeld(
            ContractClimber(self.climber)
        )

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected() 
