import commands2
from subsystems.climber import Climber

# Execute commands from the joystick axes
class ExtendClimber(commands2.CommandBase):
    def __init__(self, climber: Climber) -> None:
        super().__init__() 
        self.climber = climber
        self.addRequirements(climber)
        
    def execute(self) -> None:
        self.climber.move_up()

    def end(self, interrupted) -> None:
        self.climber.stop()

class ContractClimber(commands2.CommandBase):
    def __init__(self, climber: Climber) -> None:
        super().__init__() 
        self.climber = climber
        self.addRequirements(climber)

    def execute(self) -> None:
        self.climber.move_down()

    def end(self, interrupted) -> None:
        self.climber.stop()
