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
        self.height = 0
        
        # Grouping 
        self.climber_controllers = [self.left_hook,self.right_hook]

    def move_up(self):
        #TODO: implementar movimentação dos motores 

        self.height += 1
        print(self.height)

    def is_height_positive(self):
        return self.height > 0

    def move_down(self):
        if not self.is_height_positive():
            return

        self.height -= 1
        print(self.height)