
# Importing libraries
import typing # Lambda Functions
import wpilib 
import constants # Constant variables from constants.py

import commands2
import commands2.button

# importação do subsistema e do comando
from subsystems.exemploSubsystem import ExemploSubsistema
from commands.exemploComando import ExemploComando

# Importing Drivetrain subsystem
from subsystems.drivetrain import Drivetrain
from commands.defaultdrivetrain import DefaultDrivetrain

from subsystems.shooter import Shooter
from commands.shootcommand import ShooterCommand

from subsystems.intakeNeck import IntakeNeck
from commands.ativarNeck import ativarNeck

from subsystems.intake_elevator import IntakeElevator 
from commands.mover_elevador_intake import IntakeElevator, MoverElevator 

# In this class, has created Drivetrain controls system
class RobotContainer:
    def __init__(self) -> None:
        self.robot_drive = Drivetrain() #Creating function

        # declarar subsistema e comando
        self.exemplo = ExemploSubsistema()

        #DECLARAR SUBSYSTEM/COMANDO DO SHOOTER
        self.shooter = Shooter()

        self.intake_elevator = IntakeElevator()
                
        self.intakeNeck_subsystem = IntakeNeck()
        
        self.joystick = wpilib.Joystick(constants.C_DRIVER_CONTROLLER) # Identifying
        
        self.robot_drive.setDefaultCommand(
            DefaultDrivetrain(
                self.robot_drive, 
                lambda: self.joystick.getRawAxis(1) * constants.C_BUFFER_X_SPEED,
                lambda: self.joystick.getRawAxis(0) * constants.C_BUFFER_Z_ROTATION,
            )
        )
    
    # aqui vcs vão configurar os botoes
    def configureButtonBindings(self):
        # Exemplo: quando pressionar um determinado subsistema, ativa-lo com 50%
        commands2.button.JoystickButton(self.joystick, 1).whenPressed(
           MoverElevator(self.intake_elevator, 0.5)
        )
        commands2.button.JoystickButton(self.joystick, 2).whenPressed(
            MoverElevator(self.intake_elevator, 0.5)
        )
        commands2.button.JoystickButton(self.joystick, 3).whenPressed(
            ativarNeck(self.intakeNeck_subsystem, 0.5)
        )
        
        commands2.button.JoystickButton(self.joystick, 4).whenPressed(
            ativarNeck(self.intakeNeck_subsystem, -0.5)
        )


        
        commands2.button.JoystickButton(self.joystick, 5).whenPressed(
            ShooterCommand(self.shooter, 1)

        )

        commands2.button.JoystickButton(self.joystick, 6).whenPressed(
            ShooterCommand(self.shooter, -1)

        )