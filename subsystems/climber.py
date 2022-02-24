# Import APIs
import ctre
import commands2
import wpilib
# Import Constants Module
import constants

class Climber(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        #Start Climber controls

        self.left_hook = ctre.WPI_VictorSPX(55)
        self.right_hook = ctre.WPI_VictorSPX(66)
        self.altura = 0
        
        # Grouping 
        self.climber_controllers = [self.left_hook,self.right_hook]

    def subir(self):
        #TODO: implementar movimentação dos motores 

        self.altura += 1
        print(self.altura)

    def ContractBotao(self):

        if(self.altura>0):
            self.altura -= 1
        print(self.altura)