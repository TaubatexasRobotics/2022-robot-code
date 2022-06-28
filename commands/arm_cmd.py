import commands2
from subsystems.arm import Arm

class IntakeUpCmd(commands2.CommandBase):
    def __init__(self, arm: Arm) -> None:
        super().__init__()
        self.arm = arm
        self.addRequirements(arm)
    
    def execute(self) -> None:
        self.arm.intake_move_up()

    def end(self, interrupted: bool) -> None:
       self.arm.intake_stop()

class IntakeDownCmd(commands2.CommandBase):
    def __init__(self, arm) -> None:
        super().__init__() 
        self.arm = arm
    
    def execute(self) -> None:
        self.arm.intake_move_down()
        
    def end(self, interrupted: bool) -> None:
       self.arm.intake_stop()
