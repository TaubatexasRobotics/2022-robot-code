import commands2

class IntakeUpCmd(commands2.CommandBase):
    def __init__(self, Arm) -> None:
        super().__init__() 
        self.Arm = Arm
    
    def execute(self) -> None:
        self.Arm.intake_move_up()

    def end(self, interrupted: bool) -> None:
       self.Arm.intake_move_stop()

class IntakeDownCmd(commands2.CommandBase):
    def __init__(self, Arm) -> None:
        super().__init__() 
        self.Arm = Arm
    
    def execute(self) -> None:
        self.Arm.intake_move_down()
        
    def end(self, interrupted: bool) -> None:
       self.Arm.intake_move_stop()
