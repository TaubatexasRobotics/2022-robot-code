import wpilib
import constants
import ctre
import commands2

class IntakeNeck(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.neck_controlador = ctre.WPI_VictorSPX(7)

    def setNeck(self, porcentagem):
        self.neck_controlador.set(porcentagem)