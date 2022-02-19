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
        self.apagar_isso = 0
        self.left_hook = ctre.WPI_VictorSPX(55)
        self.right_hook = ctre.WPI_VictorSPX(66)
        
        # Grouping 
        self.climber_controllers = [self.left_hook,self.right_hook]

    def ExtendBotao(self):
        #TODO: implementar movimentação dos motores 

        print(self.apagar_isso)
        self.apagar_isso += 1

    def ContractBotao(self):

        print(self.apagar_isso)
        self.apagar_isso -= 1