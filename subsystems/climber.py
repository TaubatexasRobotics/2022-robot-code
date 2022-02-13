import ctre
import constants
import commands2
import wpilib

class Climber(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.compressor = wpilib.Compressor(wpilib.PneumaticsModuleType.CTREPCM)
        self.solenoid = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM, 
            constants.C_SOLENOID_FORWARD_CHANNEL, 
            constants.C_SOLENOID_REVERSE_CHANNEL
            )
    
    def setCompressor(self, active : bool):
        if active == True:
            self.compressor.start()
        else:
            self.compressor.stop()
        
    def setSolenoidState(self, state : int):
        self.solenoid.set({
            1 : wpilib.DoubleSolenoid.Value.kOff,
            2 : wpilib.DoubleSolenoid.Value.kForward,
            3 : wpilib.DoubleSolenoid.Value.kReverse,
        }[state])
        
        '''
        if self.stick.getRawButton(2) == True:
           self.solenoid.set(wpilib.DoubleSolenoid.Value.kOff)
        if self.stick.getRawButton(3) == True:
            self.solenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        if self.stick.getRawButton(4) == True:
            self.solenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        '''
        
        