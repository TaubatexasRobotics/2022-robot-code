# Import APIs
import ctre
import commands2
import wpilib

# Import Constants Module
import constants

class Climber(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        #Start Climber controls
        self.m_left_hook = ctre.WPI_VictorSPX(constants.C_M_LEFT_HOOK)
        #self.m_right_hook = ctre.WPI_VictorSPX(constants.C_M_RIGHT_HOOK)
        self.m_right_hook = wpilib.PWMMotorController("right",0)

        self.m_climber = wpilib.SpeedControllerGroup(self.m_left_hook, self.m_right_hook)

    def move_up(self) -> None:
        self.m_climber.set(1)

    def move_down(self) -> None:
        self.m_climber.set(-1)

    def stop(self) -> None:
        self.m_climber.set(0)
