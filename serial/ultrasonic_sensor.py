from wpilib import SerialPort
import constants

class UltrasonicSensor:
    def __init__(self) -> None:
        self.arduino = SerialPort(constants.C_BAUD_RATE, constants.C_ROBORIO_USB)
    
    # Reads distance (string) and converts to number
    def getDistance(self) -> float:
        distance = self.readString(self.arduino)
        return distance
    
    # Reading bytes from Arduino and decoding to string
    def readString(self, port : SerialPort)-> str:
        sz = port.getBytesReceived()
        buf = bytearray(sz)
        sz = port.read(buf)
        return buf[:sz].decode("ascii")