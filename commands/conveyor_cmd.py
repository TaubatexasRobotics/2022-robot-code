import commands2
from subsystems.conveyor import Conveyor

class ConveyorForwardCmd(commands2.CommandBase):
    def __init__(self, arm: Conveyor) -> None:
        super().__init__()
        self.conveyor = conveyor
        self.addRequirements(conveyor)
    
    def execute(self) -> None:
        self.conveyor.forward()

    def end(self, interrupted: bool) -> None:
       self.conveyor.stop()

class ConveyorBackwardCmd(commands2.CommandBase):
    def __init__(self, arm: Conveyor) -> None:
        super().__init__()
        self.conveyor = conveyor
        self.addRequirements(conveyor)
    
    def execute(self) -> None:
        self.conveyor.backward()

    def end(self, interrupted: bool) -> None:
       self.conveyor.stop()