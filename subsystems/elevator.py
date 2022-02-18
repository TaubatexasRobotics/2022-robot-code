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
    
  



