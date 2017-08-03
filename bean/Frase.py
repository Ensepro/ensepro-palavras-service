"""
@project PalavrasHttpEndpoint
@since 02/08/2017
@author Alencar Rodrigo Hentges <alencarhentges@gmail.com>

"""

import sys
from .Palavra import Palavra

class Frase(object):

    def __init__(self, retorno_palavras):
        self.palavras = []
        for i in range(len(retorno_palavras)):
            self.palavras.append(Palavra(i, retorno_palavras[i]))

