from basejoystick import BaseJoystick
from wpilib import XboxController
from commands2 import CommandBase
from commands2.button import JoystickButton, POVButton

class OfficialXboxController(BaseJoystick):
    
    # Constructor
    def __init__(self, xboxController : XboxController) -> None:
        super().__init__() # Call BaseJoystick Constructor
        self.xboxController = xboxController

    def getLeftStickX(self) -> float:
        return self.xboxController.getLeftX()
    
    def getLeftStickY(self) -> float:
        return self.xboxController.getLeftY()

    def getRightStickX(self) -> float:
        return self.xboxController.getRightX()

    def getRightStickY(self) -> float:
        return self.xboxController.getRightY()
    
    @BaseJoystick.intakeCommand.setter
    def intakeCommand(self, newIntakeCommand : CommandBase) -> None:
        BaseJoystick.show(self, newIntakeCommand)
        JoystickButton.(self.xboxController, XboxController.kLeftBumper).whenHeld(newIntakeCommand)
    
    @BaseJoystick.outtakeCommand.setter
    def outtakeCommand(self, newOuttakeCommand : CommandBase) -> None:
        BaseJoystick.show(self, newOuttakeCommand)
        JoystickButton.(self.xboxController, XboxController.kRightBumper).whenHeld(newOuttakeCommand)
    
    @BaseJoystick.armUpCommand.setter
    def armUpCommand(self, newArmUpCommand : CommandBase) -> None:
        BaseJoystick.show(self, newArmUpCommand)
        JoystickButton.(self.xboxController, XboxController.kLeftBumper).whenHeld(newOuttakeCommand)
