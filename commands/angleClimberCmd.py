import commands2

# Execute commands from the joystick axes
class IncreaseClimberAngle(commands2.CommandBase):
    def __init__(self, angle) -> None:
        super().__init__() 
        self.angle = angle
        
    def execute(self) -> None:
        self.angle.angle_increase()

    def end(self, interrupted):
        self.angle.stop_angle()

class DecreaseClimberAngle(commands2.CommandBase):
    def __init__(self, angle) -> None:
        super().__init__() 
        self.angle = angle

    def execute(self) -> None:
        self.angle.anlge_decrease()

    def end(self, interrupted):
        self.angle.stop_angle()