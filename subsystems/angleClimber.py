# Import APIs
import ctre
import commands2
import wpilib
# Import Constants Module
import constants

class AngleClimber(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        self.m_angle_hook = ctre.WPI_VictorSPX(constants.C_M_ANGLE_HOOK)

    def angle_increase(self):
        self.m_angle_hook.set(1)

        print("angulo aumenta")

    def anlge_decrease(self):
        self.m_angle_hook.set(-1)

        print("angulo diminui")

    def stop_angle(self):
        self.m_angle_hook.set(0)

        print("angulo parado")