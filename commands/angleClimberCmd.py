import commands2

# Execute commands from the joystick axes
class AngleClimberForward(commands2.CommandBase):
    def __init__(self, angle) -> None:
        super().__init__() 
        self.angle = angle
        
    def execute(self) -> None:
        self.angle.angle_forward()

    def end(self, interrupted):
        self.angle.stop_angle()

class AngleClimberBackward(commands2.CommandBase):
    def __init__(self, angle) -> None:
        super().__init__() 
        self.angle = angle

    def execute(self) -> None:
        self.angle.angle_backward()

    def end(self, interrupted):
        self.angle.stop_angle()