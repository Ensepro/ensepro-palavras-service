"""
@project PalavrasHttpEndpoint
@since 02/08/2017
@author Alencar Rodrigo Hentges <alencarhentges@gmail.com>

"""
from docutils.nodes import container

from configuracoes import configuracoes
from servicos.Palavras import app

if __name__ == '__main__':
    app.run(
            debug=configuracoes["servico"]["debug"],
            port=configuracoes["servico"]["porta"]
            )


