# Import APIs
import ctre
import commands2
import wpilib
# Import Constants Module
import constants

class Climber(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        #Start Climber controls
        self.m_left_hook = ctre.WPI_VictorSPX(constants.C_M_LEFT_HOOK)
        self.m_right_hook = ctre.WPI_VictorSPX(constants.C_M_RIGHT_HOOK)

        self.m_climber = wpilib.SpeedControllerGroup(self.m_left_hook, self.m_right_hook)

        self.height = 0

    def move_up(self):
        self.m_climber.set(1)

        print("subindo")

    def move_down(self):
        self.m_climber.set(-1)

        print("descendo")

    def stop(self):
        self.m_climber.set(0)
        
        print("parado")