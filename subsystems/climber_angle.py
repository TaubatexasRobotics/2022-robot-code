# Import APIs
import ctre
import commands2
from wpilib import SpeedControllerGroup
# Import Constants Module
import constants

class ClimberAngle(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.m_left_angle_hook = ctre.WPI_VictorSPX(constants.C_M_LEFT_ANGLE_HOOK)
        self.m_right_angle_hook = ctre.WPI_VictorSPX(constants.C_M_RIGHT_ANGLE_HOOK)

        self.m_climber_angle = SpeedControllerGroup(self.m_left_angle_hook, self.m_right_angle_hook)

    def angle_forward(self) -> None:
        self.m_climber_angle.set(1)

    def angle_backward(self) -> None:
        self.m_climber_angle.set(-1)

    def stop_angle(self) -> None:
        self.m_climber_angle.set(0)
