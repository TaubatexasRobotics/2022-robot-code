import ctre
import commands2
import constants

class Intake(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.m_intake = ctre.WPI_VictorSPX(constants.C_M_INTAKE)

    def intake_pull(self):
        self.m_intake.set(1)

    def intake_push(self):
        self.m_intake.set(-1)

    def intake_stop(self):
        self.m_intake.set(0)