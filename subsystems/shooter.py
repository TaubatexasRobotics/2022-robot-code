import ctre
import constants
import wpilib
import commands2

class Shooter(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        #Shooter
        self.shooter_motor = ctre.WPI_VictorSPX(8)

    def SetShooting(self, percent):
        self.shooter_motor.set(percent)


