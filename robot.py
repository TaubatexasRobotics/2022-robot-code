import wpilib
import commands2

# Véio: IterativeRobot ou TimedRobot
# Novo: TimedCommandRobot

from robotcontainer import RobotContainer

class TaubatexasRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()

if __name__ == '__main__':
    wpilib.run(TaubatexasRobot) 
