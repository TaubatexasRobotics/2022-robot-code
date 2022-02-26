import ctre
import wpilib
import commands2
import constants

class intakeActive(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.m_intakeActive = ctre.WPI_VictorSPX(constants.C_M_ACTIVATE_INTAKE)
        
        self.m_intakeActive = wpilib.SpeedControllerGroup(self.m_intakeActive)

    def pull(self):

        self.m_intakeActive.set(1)

    def push(self):

        self.m_intakeActive.set(-1)