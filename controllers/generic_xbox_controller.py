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
        return self.controller.getRawAxis(g_xbox_360['left-x-stick'])
    
    def getLeftStickY(self) -> float:
        return self.controller.getRawAxis(g_xbox_360['left-y-stick'])

    def getRightStickX(self) -> float:
        return self.controller.getRawAxis(g_xbox_360['right-x-stick'])

    def getRightStickY(self) -> float:
        return self.controller.getRawAxis(g_xbox_360['right-y-stick'])

    # Get Triggers (Axis)
    def getLeftTrigger(self) -> float:
        return self.controller.getRawAxis(g_xbox_360['lt'])

    def getRightTrigger(self) -> float:
        return self.controller.getRawAxis(g_xbox_360['rt'])

    # Getters (POVs)
    def getPOVUp(self) -> int:
        return g_xbox_360['pov-up']
    
    def getPOVRight(self) -> int:
        return g_xbox_360['pov-right']
    
    def getPOVDown(self) -> int:
        return g_xbox_360['pov-down']

    def getPOVLeft(self) -> int:
        return g_xbox_360['pov-left']

    # Setup Commands
    def setupIntakeCommand(self, newIntakeCommand : CommandBase) -> None:
        JoystickButton(self.controller, g_xbox_360['lb']).whenHeld(newIntakeCommand)
    
    def setupOuttakeCommand(self, newOuttakeCommand : CommandBase) -> None:
        JoystickButton(self.controller, g_xbox_360['rb']).whenHeld(newOuttakeCommand)
    
    def setupConveyorForwardCommand(self, newConveyorForwardCommand : CommandBase) -> None:
        JoystickButton(self.controller, g_xbox_360['a']).whenHeld(newConveyorForwardCommand)
    
    def setupConveyorBackwardCommand(self, newConveyorBackwardCommand : CommandBase) -> None:
        JoystickButton(self.controller, g_xbox_360['b']).whenHeld(newConveyorBackwardCommand)
    
    def setupExtendClimberCommand(self, newExtendClimberCommand : CommandBase) -> None:
        POVButton(self.controller, self.getPOVUp()).whenHeld(newExtendClimberCommand)

    def setupContractClimberCommand(self, newContractClimberCommand : CommandBase) -> None:
        POVButton(self.controller, self.getPOVDown()).whenHeld(newContractClimberCommand)

    def setupClimberAngleForwardCommand(self, newClimberAngleForwardCommand : CommandBase) -> None:
        POVButton(self.controller, self.getPOVRight()).whenHeld(newClimberAngleForwardCommand)

    def setupClimberAngleBackwardCommand(self, newClimberAngleBackwardCommand : CommandBase) -> None:
        POVButton(self.controller, self.getPOVLeft()).whenHeld(newClimberAngleBackwardCommand)
