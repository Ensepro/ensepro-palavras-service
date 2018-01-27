"""
@project PalavrasHttpEndpoint
@since 02/08/2017
@author Alencar Rodrigo Hentges <alencarhentges@gmail.com>

"""

import json
from constantes.StringConstantes import UTF_8

fromFile = "../configuracoes/configuracoes.json"

"""
Carrega as configurações do arquivo 'fromFile' (deve estar no formato json)
:param fromFile:
:return:
"""
configuracoes = json.loads(open(fromFile, 'r', encoding=UTF_8).read())


def getScriptTerminal() -> str:
    return configuracoes["script"]
