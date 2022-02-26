import wpilib
import constants
import ctre
import commands2

class ExemploSubsystem(commands2.SubsystemBase):
    def __init__(self):
        # instanciar construtor
        super().__init__()
        # coloquem nome relacionado a ação
        self.exemplo_controlador = ctre.WPI_VictorSPX(5)
    
    # ação precisa ser relacionado
    def setAcao(self, porcentagem):
        self.exemplo_controlador.set(porcentagem)