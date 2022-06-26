from controllers.base_controller import BaseController
from wpilib.interfaces import GenericHID
from commands2 import CommandBase
from commands2.button import JoystickButton, POVButton
from .buttons import g_xbox_360

class GenericXboxController(BaseController):
    # Constructor
    def __init__(self, port : int) -> None:
        super().__init__() # Call BaseController Constructor
        self.controller = GenericHID(port)
    
    # Getters (Stick Axis)
    def getLeftStickX(self) -> float:
        return self.controller.getRawAxis(0)
    
    def getLeftStickY(self) -> float:
        return self.controller.getRawAxis(1)

    def getRightStickX(self) -> float:
        return self.controller.getRawAxis(4)

    def getRightStickY(self) -> float:
        return self.controller.getRawAxis(5)

    # Get Triggers (Axis)
    @abstractmethod
    def getLeftTrigger(self) -> float:
        return self.controller.getRawAxis(2)

    @abstractmethod
    def getRightTrigger(self) -> float:
        return self.controller.getRawAxis(3)

    # Getters (POVs)
    def getPOVUp(self) -> float:
        return self.controller.getPOV(0)
    
    def getPOVRight(self) -> float:
        return self.controller.getPOV(90)
    
    def getPOVDown(self) -> float:
        return self.controller.getPOV(180)

    def getPOVLeft(self) -> float:
        return self.controller.getPOV(270)

    # Setup Commands
    def setupIntakeCommand(self, newIntakeCommand : CommandBase) -> None:
        JoystickButton(self.controller, g_xbox_360['lb']).whenHeld(newIntakeCommand)
    
    def setupOuttakeCommand(self, newOuttakeCommand : CommandBase) -> None:
        JoystickButton(self.controller, g_xbox_360['rb']).whenHeld(newOuttakeCommand)
    
    def setupArmUpCommand(self, newArmUpCommand : CommandBase) -> None:
        JoystickButton(self.controller, g_xbox_360['a']).whenHeld(newArmUpCommand)
    
    def setupArmDownCommand(self, newArmDownCommand : CommandBase) -> None:
        JoystickButton(self.controller, g_xbox_360['b']).whenHeld(newArmDownCommand)
    
    def setupExtendClimberCommand(self, newExtendClimberCommand : CommandBase) -> None:
        JoystickButton(self.controller, self.getPOVUp()).whenHeld(newExtendClimberCommand)
    
    def setupContractClimberCommand(self, newContractClimberCommand : CommandBase) -> None:
        JoystickButton(self.controller, self.getPOVDown()).whenHeld(newContractClimberCommand)

    def setupClimberAngleForwardCommand(self, newClimberAngleForwardCommand : CommandBase) -> None:
        JoystickButton(self.controller, self.getPOVRight()).whenHeld(newClimberAngleForwardCommand)
    
    def setupClimberAngleBackwardCommand(self, newClimberAngleBackwardCommand : CommandBase) -> None:
        JoystickButton(self.controller, self.getPOVLeft()).whenHeld(newClimberAngleBackwardCommand)