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


# Opening json
f = open('buttons.json')
button = json.load(f)

# Load respective buttons
g_xbox_360 = button['g_xbox_360']
dualshock4 = button['dualshock_4']

# class that contains all subsystems, commands and setup
class RobotContainer:
    def __init__(self) -> None:
        
        # Subsystems
        self.drivetrain = Drivetrain()
        self.climber = Climber()
        self.angle = ClimberAngle()
        self.arm = Arm()
        self.intake = Intake()
        
        # Joystick
        self.joystick = wpilib.Joystick(constants.C_DRIVER_CONTROLLER)
        
        # Drivetrain: binding command to joystick
        self.drivetrain.setDefaultCommand(
            DrivetrainCmd(
                self.drivetrain, 
                lambda: self.joystick.getRawAxis(1) * constants.C_BUFFER_X_SPEED,
                lambda: self.joystick.getRawAxis(0) * constants.C_BUFFER_Z_ROTATION,
            )
        )

    # Binding commands to joystick buttons (Except for Drivetrain)
    def configureButtonBindings(self) -> None:

        # Arm Up
        commands2.button.JoystickButton(self.joystick, g_xbox_360['a']).whenHeld(
            IntakeUpCmd(self.arm)
        )
        # Arm Down
        commands2.button.JoystickButton(self.joystick, g_xbox_360['y']).whenHeld( 
            IntakeDownCmd(self.arm)
        )

        # Pull cargo in
        commands2.button.JoystickButton(self.joystick, g_xbox_360['lb']).whenHeld( 
            IntakePullCmd(self.intake)
        )
        # Push cargo out
        commands2.button.JoystickButton(self.joystick, g_xbox_360['rb']).whenHeld( 
            IntakePushCmd(self.intake)
        )

        # Climber (hooks) Up
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

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()