import typing
import wpilib
import constants

from subsystems.drivetrain import Drivetrain
from commands.defaultdrivetrain import DefaultDrivetrain

class RobotContainer:
    def __init__(self) -> None:
        self.robot_drive = Drivetrain()

        self.joystick = wpilib.Joystick(constants.C_DRIVER_CONTROLLER)
        self.robot_drive.setDefaultCommand(
            DefaultDrivetrain(
                self.robot_drive,
                lambda: self.joystick.getRawAxis(1) * constants.C_BUFFER_X_SPEED,
                lambda: self.joystick.getRawAxis(0) * constants.C_BUFFER_Z_ROTATION,
            )
        )
