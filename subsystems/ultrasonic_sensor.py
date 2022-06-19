import commands2
import wpilib
import constants

class UltrasonicSensor(commands2.SubsystemBase):
    def __init__(self) -> None:
        self.arduino = wpilib.SerialPort(constants.C_BAUD_RATE, wpilib.SerialPort.Port.kUSB1)
    
    def getDistance(self) -> str:
        pass