
import sys

from constantes.DockerConstantes import DOCKER_EXECUTE
from constantes.DockerConstantes import DOCKER_START
from constantes.StringConstantes import BREAK_LINE
from constantes.StringConstantes import TAB
from utils import TerminalUtil
from utils import StringUtil

class DockerUtil(object):

    def __init__(self, nomeContainer):
        self.nomeContainer = nomeContainer

    def initContainer(self, params):
        try:
            print("Inicializando container...")
            resultadoTerminal = TerminalUtil.getResultadoTerminalUTF8(self._prepararComando(True, params))
            resultadoOK = StringUtil.removeStrings([BREAK_LINE, TAB], resultadoTerminal, "")
        except Exception as ex:
            resultadoOK = ex
        if (resultadoOK == self.nomeContainer):
            print("Conteiner '" + self.nomeContainer + "' foi iniciado ou já esta em execução!\n")
        else:
            print(resultadoOK)
            sys.exit("Não foi possível iniciar o container '" + self.nomeContainer + "':")


    def _prepararComando(self, isStartCommand, params):
        if(isStartCommand):
            comando = DOCKER_START.replace("?", self.nomeContainer)
        else:
            comando = DOCKER_EXECUTE.replace("?", self.nomeContainer)

        for param in params:
            comando = comando + " " + param

        return comando

    def dockerExec(self, params):
        comando = self._prepararComando(False, params)
        # print("Executando comando: "+comando)
        resultadoTerminal = TerminalUtil.getResultadoTerminalUTF8(comando)
        # print(resultadoTerminal)
        return resultadoTerminal