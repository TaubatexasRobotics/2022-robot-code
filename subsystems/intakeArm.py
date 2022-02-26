import ctre
import wpilib
import commands2
import constants

class intakeArm(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.m_intakeArm = ctre.WPI_VictorSPX(constants.C_M_ARM_INTAKE)
        
        self.m_intakeArm = wpilib.SpeedControllerGroup(self.m_intakeArm)

    def move_up(self):

        self.m_intakeArm.set(1)

    def move_down(self):

        self.m_intakeArm.set(-1)