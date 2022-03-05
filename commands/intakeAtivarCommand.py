import commands2

from subsystems.intakeAtivar import intakeActive

class PullIntake(commands2.CommandBase):
    def __init__(self, intakeActive) -> None:
        super().__init__() 
        self.intakeActive = intakeActive
    def execute(self) -> None:
        self.intake.pull()


class PushIntake(commands2.CommandBase):
    def __init__(self, intakeActive) -> None:
        super().__init__() 
        self.intakeActive = intakeActive
    


