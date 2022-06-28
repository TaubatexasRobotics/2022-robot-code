# RobotPy
import wpilib

# Command-based robot
import commands2
import commands2.button

# Easily managing our constants
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
        self.joystick = GenericXboxController(constants.C_DRIVER_CONTROLLER)

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
        # Pull cargo in
        self.joystick.setupIntakeCommand(IntakePullCmd(self.intake))

        # Push cargo out
        self.joystick.setupOuttakeCommand(IntakePushCmd(self.intake))

        # Arm Up
        self.joystick.setupArmUpCommand(IntakeUpCmd(self.arm))

        # Arm Down
        self.joystick.setupArmDownCommand(IntakeDownCmd(self.arm))
        
        # Climber (hooks) Up
        self.joystick.setupExtendClimberCommand(ExtendClimber(self.climber))
        
        # Climber (hooks) Down
        #self.joystick.setupContractClimberCommand(ContractClimber(self.climber))
        
        # Climber leans forward
        #self.joystick.setupClimberAngleForwardCommand(ClimberAngleForward(self.angle))

        # Climber leans backward
        #self.joystick.setupClimberAngleBackwardCommand(ClimberAngleBackward(self.angle))

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected() 