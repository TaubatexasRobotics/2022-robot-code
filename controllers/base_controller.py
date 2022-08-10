from commands2 import CommandBase
from abc import ABC, abstractmethod

class BaseController(ABC):
    # Constructor
    def __init__(self) -> None:
        self.__intakeCommand = None
        self.__outtakeCommand = None
        self.__conveyorForwardCommand = None
        self.__conveyorBackwardCommand = None
        self.__extendClimberCommand = None
        self.__contractClimberCommand = None
        self.__climberAngleForwardCommand = None
        self.__climberAngleBackwardCommand = None

    # Getters (Stick Axis)
    @abstractmethod
    def getLeftStickX(self) -> float:
        pass

    @abstractmethod
    def getLeftStickY(self) -> float:
        pass

    @abstractmethod
    def getRightStickX(self) -> float:
        pass

    @abstractmethod
    def getRightStickY(self) -> float:
        pass
    
    # Get Triggers (Axis)
    @abstractmethod
    def getLeftTrigger(self) -> float:
        pass

    @abstractmethod
    def getRightTrigger(self) -> float:
        pass    

    # Getters (POVs)
    @abstractmethod
    def getPOVUp(self) -> int:
        pass

    @abstractmethod
    def getPOVDown(self) -> int:
        pass

    @abstractmethod
    def getPOVLeft(self) -> int:
        pass

    @abstractmethod
    def getPOVRight(self) -> int:
        pass

    # Getters (Commands)
    @property
    def intakeCommand(self) -> CommandBase:
        return self.__intakeCommand

    @property
    def outtakeCommand(self) -> CommandBase:
        return self.__outtakeCommand
    
    @property
    def conveyorForwardCommand(self) -> CommandBase:
        return self.__conveyorForwardCommand

    @property
    def conveyorBackwardCommand(self) -> CommandBase:
        return self.__conveyorBackwardCommand
    
    @property
    def extendClimberCommand(self) -> CommandBase:
        return self.__extendClimberCommand
    
    @property
    def extendClimberCommand(self) -> CommandBase:
        return self.__extendClimberCommand

    @property
    def contractClimberCommand(self) -> CommandBase:
        return self.__contractClimberCommand

    @property
    def climberAngleForwardCommand(self) -> CommandBase:
        return self.__climberAngleForwardCommand

    @property
    def climberAngleBackwardCommand(self) -> CommandBase:
        return self.__climberAngleBackwardCommand

    # Setters (Commands)
    @intakeCommand.setter
    def intakeCommand(self, newIntakeCommand : CommandBase) -> None:
        self.__intakeCommand = newIntakeCommand
    
    @outtakeCommand.setter
    def outtakeCommand(self, newOuttakeCommand : CommandBase) -> None:
        self.__outtakeCommand = newOuttakeCommand
    
    @conveyorForwardCommand.setter
    def conveyorForwardCommand(self, newConveyorForwardCommand : CommandBase) -> None:
        self.__conveyorForwardCommand = newConveyorForwardCommand

    @conveyorBackwardCommand.setter
    def conveyorBackwardCommand(self, newConveyorBackwardCommand : CommandBase) -> None:
        self.__conveyorBackwardCommand = newConveyorBackwardCommand

    @extendClimberCommand.setter
    def extendClimberCommand(self, newExtendClimberCommand : CommandBase) -> None:
        self.__extendClimberCommand = newExtendClimberCommand

    @contractClimberCommand.setter
    def contractClimberCommand(self, newContractClimberCommand : CommandBase) -> None:
        self.__contractClimberCommand = newContractClimberCommand

    @climberAngleForwardCommand.setter
    def climberAngleForwardCommand(self, newClimberAngleForwardCommand : CommandBase) -> None:
        self.__climberAngleForwardCommand = newClimberAngleForwardCommand

    @climberAngleBackwardCommand.setter
    def climberAngleBackwardCommand(self, newClimberAngleBackwardCommand : CommandBase) -> None:
        self.__climberAngleBackwardCommand = newClimberAngleBackwardCommand

    # Setup Commands
    @abstractmethod
    def setupIntakeCommand(self, newIntakeCommand : CommandBase) -> None:
        pass
    
    @abstractmethod
    def setupOuttakeCommand(self, newOuttakeCommand : CommandBase) -> None:
        pass
    
    @abstractmethod
    def setupConveyorForwardCommand(self, newConveyorForwardCommand : CommandBase) -> None:
        pass
    
    @abstractmethod
    def setupConveyorBackwardCommand(self, newConveyorBackwardCommand : CommandBase) -> None:
        pass
    
    @abstractmethod
    def setupExtendClimberCommand(self, newExtendClimberCommand : CommandBase) -> None:
        pass
    
    @abstractmethod
    def setupContractClimberCommand(self, newContractClimberCommand : CommandBase) -> None:
        pass

    @abstractmethod
    def setupClimberAngleForwardCommand(self, newClimberAngleForwardCommand : CommandBase) -> None:
        pass
    
    @abstractmethod
    def setupClimberAngleBackwardCommand(self, newClimberAngleBackwardCommand : CommandBase) -> None:
        pass