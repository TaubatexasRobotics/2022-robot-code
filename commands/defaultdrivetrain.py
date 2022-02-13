import typing
import commands2
from subsystems.drivetrain import Drivetrain

class DefaultDrivetrain(commands2.CommandBase):
    def __init__(self, robot_drive : Drivetrain, x_speed : typing.Callable[[], float], z_rotation : typing.Callable[[], float]) -> None:
        super().__init__() 
        self.robot_drive = robot_drive
        self.x_speed = x_speed
        self.z_rotation = z_rotation
        
        self.addRequirements([self.robot_drive])

    def execute(self) -> None:
        self.robot_drive.setMotors(self.x_speed(), self.z_rotation()