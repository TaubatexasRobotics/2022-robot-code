import typing
import commands2

from subsystems.intakeNeck import IntakeNeck

class ativarNeck(commands2.CommandBase):
    def __init__(self, intakeNeck, porcentagem) -> None:
        super().__init__()
        self.intakeNeck = intakeNeck
        self.porcentagem = porcentagem

    def execute(self) -> None:
        self.intakeNeck.setNeck(self.porcentagem)
