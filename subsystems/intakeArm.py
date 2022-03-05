import ctre
import commands2
import constants

class IntakeArm(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.m_intakeArm = ctre.WPI_VictorSPX(constants.C_M_ARM_INTAKE)

    def intake_move_up(self):

        self.m_intakeArm.set(1)
        print("sobe")

    def intake_move_down(self):

        self.m_intakeArm.set(-1)
        print("desce")
    
    def intake_move_stop(self):
        self.m_intakeArm.set(0)
        print("para")