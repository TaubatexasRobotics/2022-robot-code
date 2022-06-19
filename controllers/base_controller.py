from commands2 import CommandBase
from abc import ABC, abstractmethod

class BaseController(ABC):
    # Constructor
    def __init__(self) -> None:
        self.__intakeCommand = None
        self.__outtakeCommand = None
        self.__armUpCommand = None
        self.__armDownCommand = None

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
    
    # Setters (Commands)
    @abstractmethod
    def setupIntakeCommand(self, newIntakeCommand : CommandBase):
        pass

    @intakeCommand.setter
    def intakeCommand(self, newIntakeCommand : CommandBase) -> None:
        self.__intakeCommand = newIntakeCommand