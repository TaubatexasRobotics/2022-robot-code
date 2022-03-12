import commands2

class IntakeUpCmd(commands2.CommandBase):
    def __init__(self, intakeArm) -> None:
        super().__init__() 
        self.intakeArm = intakeArm
    
    def execute(self) -> None:
        self.intakeArm.intake_move_up()

    def end(self, interrupted: bool) -> None:
       self.intakeArm.intake_move_stop()

class IntakeDownCmd(commands2.CommandBase):
    def __init__(self, intakeArm) -> None:
        super().__init__() 
        self.intakeArm = intakeArm
    
    def execute(self) -> None:
        self.intakeArm.intake_move_down()
        
    def end(self, interrupted: bool) -> None:
       self.intakeArm.intake_move_stop()
