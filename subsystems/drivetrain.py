# Importing libraries and constant values
import ctre
import constants # Values from constants.py
import commands2
import wpilib
import wpilib.drive

# Drivetrain subsystem class
class Drivetrain(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        
        # Controls for Drivetrain system
        self.m_left_front = ctre.WPI_VictorSPX(constants.C_M_LEFT_FRONT)
        self.m_right_front = ctre.WPI_VictorSPX(constants.C_M_RIGHT_FRONT)
        self.m_left_back = ctre.WPI_VictorSPX(constants.C_M_LEFT_BACK)
        self.m_right_back = ctre.WPI_VictorSPX(constants.C_M_RIGHT_BACK)
        
        self.m_left = wpilib.SpeedControllerGroup(self.m_left_front, self.m_left_back)
        self.m_right = wpilib.SpeedControllerGroup(self.m_right_front, self.m_right_back)
	
        self.robot_drive = wpilib.drive.DifferentialDrive(self.m_left, self.m_right)
        self.robot_drive.setExpiration(0.1)
   	
    # Enable Safety
    def enableSafety(self, state : bool) -> None:
        self.robot_drive.setSafetyEnabled(state)

    # Function for start motors (arcade drive)
    def setMotorsArcadeDrive(self, x_speed : float, z_rotation : float, square_inputs : bool) -> None:
        self.robot_drive.arcadeDrive(x_speed, z_rotation, square_inputs)

    # Function for start motors (curvature drive)
    def setMotorsCurvatureDrive(self, x_speed : float, z_rotation : float, allow_turn_in_place : bool) -> None:
        self.robot_drive.curvatureDrive(x_speed, z_rotation, allow_turn_in_place)

    # Function for start motors (tank drive)
    def setMotorsTankDrive(self, left_speed : float, right_speed : float, square_inputs : bool) -> None:
        self.robot_drive.tankDrive(left, right, square_inputs)

