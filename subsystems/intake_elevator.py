import ctre
import constants
import commands2
import wpilib

class IntakeElevator(commands2.SubsystemBase):
    def __init__(self): 
        super().__init__()
        self.elevator_controlador = ctre.WPI_VictorSPX(6)
    def setAcao(self, porcentagem):
        self.elevator_controlador.set(porcentagem)
