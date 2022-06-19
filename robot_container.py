# Not sure yet about these two :)
# import typing # Lambda Functions
# from commands2 import button 

# RobotPy
import wpilib

# JSON
import json

# Command-based robot
import commands2
import commands2.button

# easily managing our constants
import constants

# Climber
from subsystems.climber import Climber
from commands.climber_cmd import ExtendClimber, ContractClimber
from subsystems.climber_angle import ClimberAngle
from commands.climber_angle_cmd import ClimberAngleForward, ClimberAngleBackward

# Drivetrain
from subsystems.drivetrain import Drivetrain
from commands.drivetrain_cmd import DrivetrainCmd

# Arm
from subsystems.arm import Arm
from commands.arm_cmd import IntakeDownCmd, IntakeUpCmd

# Intake
from subsystems.intake import Intake
from commands.intake_cmd import IntakePushCmd, IntakePullCmd

# Controllers
from controllers.generic_xbox_controller import GenericXboxController
from controllers.dualshock4_controller import DualShock4Controller

# Class that contains all subsystems, commands and setup
class RobotContainer:
    def __init__(self) -> None:   
        # Subsystems
        self.drivetrain = Drivetrain()
        self.climber = Climber()
        self.angle = ClimberAngle()
        self.arm = Arm()
        self.intake = Intake()
        
        # Joystick
        self.joystick = DualShock4Controller(constants.C_DRIVER_CONTROLLER)

        # Drivetrain: binding command to joystick
        self.drivetrain.setDefaultCommand(
            DrivetrainCmd(
                self.drivetrain, 
                lambda: self.joystick.getLeftStickY() * constants.C_BUFFER_X_SPEED,
                lambda: self.joystick.getLeftStickX() * constants.C_BUFFER_Z_ROTATION,
            )
        )

    # Binding commands to joystick buttons (Except for Drivetrain)
    def configureButtonBindings(self) -> None:
        self.joystick.setupIntakeCommand(IntakePullCmd(self.intake))
        #self.joystick.outtakeCommand = IntakePushCmd(self.intake)
        #self.joystick.armUpCommand = IntakeUpCmd(self.arm)
        #self.joystick.armDownCommand = IntakeDownCmd(self.arm)

        # Climber (hooks) Up
        '''
        commands2.button.POVButton(self.joystick, 0).whenHeld(
            ExtendClimber(self.climber)
        )
        # Climber (hooks) Down
        commands2.button.POVButton(self.joystick, 180).whenHeld(
            ContractClimber(self.climber)
        )

        # Climber leans forward
        commands2.button.POVButton(self.joystick, 90).whenHeld(
            ClimberAngleForward(self.angle)
        )

        # Climber leans backward
        commands2.button.POVButton(self.joystick, 270).whenHeld(
            ClimberAngleBackward(self.angle)
        )
        '''
    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected() 
