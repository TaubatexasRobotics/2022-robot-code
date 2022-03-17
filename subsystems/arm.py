import ctre
import commands2
import constants

class Arm(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.m_Arm = ctre.WPI_VictorSPX(constants.C_M_ARM)

    def intake_move_up(self) -> None:
        self.m_Arm.set(1)

    def intake_move_down(self) -> None:
        self.m_Arm.set(-1)
    
    def intake_move_stop(self) -> None:
        self.m_Arm.set(0)
