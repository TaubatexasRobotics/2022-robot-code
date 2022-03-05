import commands2

from subsystems.intakeRolamento import IntakeRolamento

class IntakePushCmd(commands2.CommandBase):
    def __init__(self, intakeRolamento) -> None:
        super().__init__() 
        self.intakeRolamento = intakeRolamento
    
    def execute(self) -> None:
        self.intakeRolamento.intake_rolamento_push()
    
    def end(self, interrupted: bool) -> None:
        self.intakeRolamento.intake_rolamento_stop()


class IntakePullCmd(commands2.CommandBase):
    def __init__(self, intakeRolamento) -> None:
        super().__init__() 
        self.intakeRolamento = intakeRolamento
    
    def execute(self) -> None:
        self.intakeRolamento.intake_rolamento_pull()
    
    def end(self, interrupted: bool) -> None:
        self.intakeRolamento.intake_rolamento_stop()
        
        


