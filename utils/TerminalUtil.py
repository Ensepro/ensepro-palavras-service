
import subprocess

from . import ConverterUtil


def executarComandoTerminal(comando):
    return subprocess.check_output(comando, shell=True)

def getResultadoTerminalUTF8(comando):
    result = executarComandoTerminal(comando)
    return ConverterUtil.toUTF8(result)