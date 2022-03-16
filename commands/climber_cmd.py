import commands2

# Execute commands from the joystick axes
class ExtendClimber(commands2.CommandBase):
    def __init__(self, climber) -> None:
        super().__init__() 
        self.climber = climber
        
    def execute(self) -> None:
        self.climber.move_up()

    def end(self, interrupted):
        self.climber.stop()

class ContractClimber(commands2.CommandBase):
    def __init__(self, climber) -> None:
        super().__init__() 
        self.climber = climber

    def execute(self) -> None:
        self.climber.move_down()

    def end(self, interrupted):
        self.climber.stop()