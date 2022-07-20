import wpilib
import constants
import decode_bytes
from serial.decode_bytes import readString

class UltrasonicSensor:
    def __init__(self) -> None:
        self.arduino = wpilib.SerialPort(constants.C_BAUD_RATE, wpilib.SerialPort.Port.kUSB1)
    
    def getDistance(self) -> str:
        readString (self.arduino)