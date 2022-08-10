import ctre
import commands2
import constants
import wpilib
class Intake(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.m_intake = ctre.WPI_VictorSPX(constants.C_M_INTAKE)
        self.limitSwitch = wpilib.DigitalInput(constants.LIMIT_SWITCH)


    def intake_pull(self) -> None:
        self.m_intake.set(1)

    def intake_push(self) -> None: 
        self.m_intake.set(-1)

    def intake_stop(self) -> None:
        self.m_intake.set(0)
