from commands2 import CommandBase
from abc import ABC, abstractmethod

class BaseController(ABC):
    # Constructor
    def __init__(self) -> None:
        self.__intakeCommand = None
        self.__outtakeCommand = None
        self.__armUpCommand = None
        self.__armDownCommand = None
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
    def getPOVUp(self) -> float:
        pass

    @abstractmethod
    def getPOVDown(self) -> float:
        pass

    @abstractmethod
    def getPOVLeft(self) -> float:
        pass

    @abstractmethod
    def getPOVRight(self) -> float:
        pass

    # Getters (Commands)
    @property
    def intakeCommand(self) -> CommandBase:
        return self.__intakeCommand

    @property
    def outtakeCommand(self) -> CommandBase:
        return self.__outtakeCommand
    
    @property
    def armUpCommand(self) -> CommandBase:
        return self.__armUpCommand

    @property
    def armDownCommand(self) -> CommandBase:
        return self.__armDownCommand
    
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
    
    @armUpCommand.setter
    def armUpCommand(self, newArmUpCommand : CommandBase) -> None:
        self.__armUpCommand = newArmUpCommand

    @armDownCommand.setter
    def armDownCommand(self, newArmDownCommand : CommandBase) -> None:
        self.__armDownCommand = newArmDownCommand

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
    def setupArmUpCommand(self, newArmUpCommand : CommandBase) -> None:
        pass
    
    @abstractmethod
    def setupArmDownCommand(self, newArmDownCommand : CommandBase) -> None:
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