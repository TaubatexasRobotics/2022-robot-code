import typing 
import commands2
from subsystems.intake_elevator import IntakeElevator

class MoverElevator(commands2.CommandBase):
    def __init__(self, intakeelevator: IntakeElevator, porcentagem) -> None:
        super().__init__()

        self.intakeelevator = intakeelevator
        self.porcentagem = porcentagem

    def execute(self) -> None:
        self.exemplo.setAcao(self.porcentagem)