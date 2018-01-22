"""
@project PalavrasHttpEndpoint
@since 02/08/2017
@author Alencar Rodrigo Hentges <alencarhentges@gmail.com>

"""

import sys
import json
from conversores import MakeJsonSerializable
from utils import StringUtil

class Palavra(object):

    def __init__(self, numero, palavra):
        self.numero = numero
        self.nivel = 0
        self.palavra_original = ""
        self.palavra_canonica = ""
        self.tags = []
        self.tag_inicial = ""

        nivelEnd = StringUtil.find(palavra, ".")
        parentesesInicio = StringUtil.find(palavra, "(")
        parentesesFim = StringUtil.find(palavra, ")")

        if (nivelEnd == -1):
            raise Exception("Erro: Formato da palavra inválido('" + palavra + "'). Palavra.__init__")

        self.nivel = palavra[:nivelEnd]
        if (parentesesInicio == -1 or parentesesFim == -1):
            self.tag_inicial = palavra[nivelEnd + 2:]
        else:
            tagsDentroParenteses = palavra[parentesesInicio + 1:(parentesesFim - len(palavra))].split()
            self.tag_inicial = palavra[nivelEnd + 2:parentesesInicio]
            self.palavra_original = palavra.split()[-1]
            self.palavra_canonica = tagsDentroParenteses[0].replace("\"", "")
            self.tags = tagsDentroParenteses[1:]

    def to_json(self):
        return self.__dict__

    def __hash__(self):
        return self.numero

    def __eq__(self, other):
        return self.numero == other.numero  # and self.palavraOriginal == other.palavraOriginal


