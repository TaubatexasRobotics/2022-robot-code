import wpilib as wpilib
slave_address = 4
Wire = wpilib.I2C(wpilib._wpilib.I2C.Port.kOnboard,slave_address)
MAX_BYTES = 32
def getData():
    data = []
    Wire.read(slave_address, MAX_BYTES, data)
    return data