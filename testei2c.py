import wpilib as wpilib
slave_address = 4
Wire = wpilib.I2C(wpilib._wpilib.I2C.Port.kOnboard,slave_address)
MAX_BYTES = 32
def getData():
    #onde será armazenada a informação recebida
    data = []

    #
    pegou = Wire.read(slave_address, MAX_BYTES, data)

    if pegou == True:
        print("informação recebida")
        print(data)