"""
@project nlu 
@class UtilFrase
@date 22/03/2017 17:43
@author Alencar Rodrigo Hentges <alencarhentges@gmail.com>
"""

from bean.Frase import Frase
from utils import DockerUtil
from utils import StringUtil
from constantes.StringConstantes import BREAK_LINE
from constantes.StringConstantes import TAB
import configuracoes


class FraseUtil(object):
    @staticmethod
    def etapa1_getResultadoPalavras(palavras: DockerUtil, frase):
        """
        Irá executar o comando "SCRIPT "frase"
        :param palavras: Objeto do tipo DockerUtil que terá o link com o container desejado.
        :param frase: frase a ser analisada
        :return: Retorna as informações sem nenehum tipo de modificação
        """
        return palavras.dockerExec([configuracoes.getScriptContainer(), "\"" + frase + "\""])

    @staticmethod
    def etapa2_removeDadosNaoNecessarios(etapa1_retorno_palavras):
        """
        Transforma o retorno do palavras em uma lista e remove dados/linhas não necessárias.
        ex: "<ß>"/"<servicos>"
        :param etapa1_retorno_palavras: Retorno do método "etapa1_getResultadoPalavras"
        :return: lista com as informações relavantes do retorno do palavras.
        """
        etapa1_retorno_palavras_list = etapa1_retorno_palavras.split(BREAK_LINE)
        listaFinal = []
        dentroA1 = False
        for i in range(len(etapa1_retorno_palavras_list)):
            if (etapa1_retorno_palavras_list[i] == 'A1'):
                dentroA1 = True
                continue

            if (dentroA1 and StringUtil.isEmpty(etapa1_retorno_palavras_list[i])):
                dentroA1 = False

            if (dentroA1):
                listaFinal.append(StringUtil.removeStrings([TAB, BREAK_LINE], etapa1_retorno_palavras_list[i], " "))

        return listaFinal

    @staticmethod
    def etapa3_trocaIgualPorNivel(etapa2_lista):
        """
        Troca os "=" no inicio das palavras pelo número de "=".
        :param etapa2_lista: lista resultante do método "etapa2_removeDadosNaoNecessarios"
        :return: lista com "numeroDe'='. ITEM DA LISTA"
        """
        return [(str(item.count("=")) + ". " + item.replace("=", "")) for item in etapa2_lista]

    @staticmethod
    def getFrase(palavras: DockerUtil, frase: str) -> Frase:
        etapa1 = FraseUtil.etapa1_getResultadoPalavras(palavras, frase)
        # print(etapa1)
        etapa2 = FraseUtil.etapa2_removeDadosNaoNecessarios(etapa1)
        etapa3 = FraseUtil.etapa3_trocaIgualPorNivel(etapa2)
        return Frase(etapa3)
