import ctre
import constants
import commands2
import wpilib

class Elevator(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()
        self.compressor = wpilib.Compressor(wpilib.PneumaticsModuleType.CTREPCM)
        self.solenoid = wpilib.DoubleSolenoid(
            wpilib.Pn
        )
    
# Function to control solenoid from the joystick
    def setSolenoidState(self, state : int):
        self.solenoid.set({
            0 : wpilib.DoubleSolenoid.Value.kOff,
            1 : wpilib.DoubleSolenoid.Value.kForward,
            2 : wpilib.DoubleSolenoid.Value.kReverse
        }[state])
  



