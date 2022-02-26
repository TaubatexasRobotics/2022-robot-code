import commands2

from subsystems.intakeArm import intake

class IntakeUp(commands2.CommandBase):
    def __init__(self, intake) -> None:
        super().__init__() 
        self.intake = intake
    def execute(self) -> None:
        self.intake.move_up()


class IntakeDown(commands2.CommandBase):
    def __init__(self, intake) -> None:
        super().__init__() 
        self.intake = intake
    def execute(self) -> None:
        self.intake.move_down()