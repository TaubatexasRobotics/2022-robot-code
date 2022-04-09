# Import APIs
import ctre
import commands2
# Import Constants Module
import constants

class ClimberAngle(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.m_angle_hook = ctre.WPI_VictorSPX(constants.C_M_ANGLE_HOOK)

    def angle_forward(self) -> None:
        self.m_angle_hook.set(1)

    def angle_backward(self) -> None:
        self.m_angle_hook.set(-1)

    def stop_angle(self) -> None:
        self.m_angle_hook.set(0)
