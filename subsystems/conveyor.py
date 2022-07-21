import ctre
import commands2
import constants

class Conveyor(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.m_conveyor = ctre.WPI_VictorSPX(constants.C_M_CONVEYOR)

    def forward(self) -> None:
        self.m_conveyor.set(1)

    def backward(self) -> None:
        self.m_conveyor.set(-1)
    
    def stop(self) -> None:
        self.m_conveyor.set(0)