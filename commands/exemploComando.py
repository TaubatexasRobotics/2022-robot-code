import typing # Parameter calling
import commands2

# aqui vcs colocam o nome do subsistema que criaram
from subsystems.exemploSubsystem import Exemplo

class Exemplo(commands2.CommandBase):
    def __init__(self, exemplo: Exemplo, porcentagem) -> None:
        super().__init__()
        # aqui vcs colocam o nome do subsistema que criaram, exatamente como lá em cima
        self.exemplo = exemplo
        self.porcentagem = porcentagem
    
    def execute(self) -> None:
        # setAcao é a ação que vcs criaram na classe do subsistema
        self.exemplo.setAcao(self.porcentagem)
    
    # dps de digitarem, abrem o robotcontainer