"""
@project PalavrasHttpEndpoint
@since 02/08/2017
@author Alencar Rodrigo Hentges <alencarhentges@gmail.com>

"""

import json
import configuracoes
from flask import Flask
from utils.DockerUtil import DockerUtil
from utils.FraseUtil import FraseUtil

palavras = DockerUtil(configuracoes.getNomeContainer())
palavras.initContainer([])

app = Flask(__name__)

@app.route('/palavras/analisar/<string:frase>',  methods=['GET'])
def analisarFrase(frase):
    frase = FraseUtil.getFrase(palavras, frase)
    return json.dumps(frase.palavras)
