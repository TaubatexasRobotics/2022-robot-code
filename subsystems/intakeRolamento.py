import ctre
import wpilib
import commands2
import constants

class IntakeRolamento(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.m_intakeRolamento = ctre.WPI_VictorSPX(constants.C_M_ROLAMENTO_INTAKE)

    def intake_rolamento_pull(self):

        self.m_intakeRolamento.set(1)
        print("sobeRolamento")

    def intake_rolamento_push(self):

        self.m_intakeRolamento.set(-1)
        print("desceRolamento")

    def intake_rolamento_stop(self):

        self.m_intakeRolamento.set(0)
        print("paraRolamento")