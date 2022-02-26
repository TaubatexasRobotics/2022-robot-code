import commands2


# Importing functions from Subsystem
#from subsystems.climber import Climber

# Execute commands from the joystick axes
class ExtendClimber(commands2.CommandBase):
    def __init__(self, climber) -> None:
        super().__init__() 
        self.climber = climber

    # def initialize(self) -> None:
    #     super().initialize()
        
    def execute(self) -> None:
        self.climber.move_up()

class ContractClimber(commands2.CommandBase):
    def __init__(self, climber) -> None:
        super().__init__() 
        self.climber = climber

    # def initialize(self) -> None:
    #     super().initialize()

    def execute(self) -> None:
        self.climber.move_down()
