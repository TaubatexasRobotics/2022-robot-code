import typing # Parameter calling
import commands2

# Importing functions from Subsystem
from subsystems.drivetrain import Drivetrain

# Executing Arcade Drive
class DrivetrainArcadeDrive(commands2.CommandBase):
    def __init__(self, 
    robot_drive : Drivetrain, x_speed : typing.Callable[[], float], 
    z_rotation : typing.Callable[[], float], square_inputs : bool) -> None:
        super().__init__() 
        self.robot_drive = robot_drive
        self.x_speed = x_speed
        self.z_rotation = z_rotation
        self.square_inputs = square_inputs
        
        self.addRequirements([self.robot_drive])

    def execute(self) -> None:
        self.robot_drive.setMotorsArcadeDrive(self.x_speed(), self.z_rotation(), self.square_inputs)

# Executing Curvature Drive
class DrivetrainCurvatureDrive(commands2.CommandBase):
    def __init__(self, 
    robot_drive : Drivetrain, x_speed : typing.Callable[[], float], 
    z_rotation : typing.Callable[[], float], allow_turn_in_place : bool) -> None:
        super().__init__() 
        self.robot_drive = robot_drive
        self.x_speed = x_speed
        self.z_rotation = z_rotation
        self.allow_turn_in_place = allow_turn_in_place
        
        self.addRequirements([self.robot_drive])

    def execute(self) -> None:
        self.robot_drive.setMotorsCurvatureDrive(self.x_speed(), self.z_rotation(), self.allow_turn_in_place)

# Executing Tank Drive
class DrivetrainTankDrive(commands2.CommandBase):
    def __init__(self, 
    robot_drive : Drivetrain, left_speed : typing.Callable[[], float], 
    right_speed : typing.Callable[[], float], square_inputs : bool) -> None:
        super().__init__() 
        self.robot_drive = robot_drive
        self.left_speed = left_speed
        self.right_speed = right_speed
        self.square_inputs = square_inputs
        
        self.addRequirements([self.robot_drive])

    def execute(self) -> None:
        self.robot_drive.setMotorsTankDrive(self.left_speed(), self.right_speed(), self.square_inputs)