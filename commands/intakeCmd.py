import commands2

class IntakePushCmd(commands2.CommandBase):
    def __init__(self, intake) -> None:
        super().__init__() 
        self.intake = intake
    
    def execute(self) -> None:
        self.intake.intake_push()
    
    def end(self, interrupted: bool) -> None:
        self.intake.intake_stop()


class IntakePullCmd(commands2.CommandBase):
    def __init__(self, intake) -> None:
        super().__init__() 
        self.intake = intake
    
    def execute(self) -> None:
        self.intake.intake_pull()
    
    def end(self, interrupted: bool) -> None:
        self.intake.intake_stop()
        
        


