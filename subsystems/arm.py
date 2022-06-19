import ctre
from wpilib import Timer
import commands2
import constants

class Arm(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.m_arm = ctre.WPI_VictorSPX(constants.C_M_ARM)
        
        self.timer = Timer()
        self.last_burst_time = 0

    def intake_move_up(self) -> None:
        self.last_burst_time = self.timer.getFPGATimestamp()
        if self.timer.getFPGATimestamp() - self.last_burst_time < constants.C_ARM_TIME_UP:
            self.m_arm.set(constants.C_ARM_TRAVEL)
        else:
            self.m_arm.set(constants.C_ARM_HOLD_UP)

    def intake_move_down(self) -> None:
        self.last_burst_time = self.timer.getFPGATimestamp()
        if self.timer.getFPGATimestamp() - self.last_burst_time < constants.C_ARM_TIME_DOWN:
            self.m_arm.set(constants.C_ARM_TRAVEL * -1)
        else:
            self.m_arm.set(constants.C_ARM_HOLD_DOWN * -1)
    
    def intake_stop(self) -> None:
        self.m_arm.set(0)