import typing
import commands2

from subsystems.shooter import Shooter

class ShooterCommand(commands2.CommandBase):
    def __init__(self, shooter, percent) -> None:
        super().__init__()
        self.shooter = shooter
        self.percent = percent

def execute(self) -> None:
    self.exemplo.SetShooting(self.percent)

