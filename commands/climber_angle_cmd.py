import commands2
from subsystems.climber_angle import ClimberAngle

# Execute commands from the joystick axes
class ClimberAngleForward(commands2.CommandBase):
    def __init__(self, angle: ClimberAngle) -> None:
        super().__init__() 
        self.angle = angle
        self.addRequirements(angle)

    def execute(self) -> None:
        self.angle.angle_forward()

    def end(self, interrupted: bool) -> None:
        self.angle.stop_angle()

class ClimberAngleBackward(commands2.CommandBase):
    def __init__(self, angle: ClimberAngle) -> None:
        super().__init__() 
        self.angle = angle
        self.addRequirements(angle)

    def execute(self) -> None:
        self.angle.angle_backward()

    def end(self, interrupted: bool) -> None:
        self.angle.stop_angle()
