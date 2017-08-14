# Palavras Service 
 
## Dependências

1. Python 3
2. Modulo `flask` (para instalar: `pip install flask`)

## Configurando serviço do zero

1. Criar o container a partir da imagem do Palavras.
1.1. `docker run -it --name palavras_service -p 8099:8099 ubuntu/palavras:11952a /bin/bash`

2. Criar o arquivo `palavrasTree` no diretório `root`
2.1. `touch palavrasTree`
2.2. Script
```
    #! /bin/bash
    export LANG=pt_BR.UTF-8
    export PERL_UNICODE=SDA
    echo $1 | /opt/palavras/por.pl | /opt/palavras/bin/dep2tree
```

3. Criar o arquivo `startPalavrasService` no diretório `root`
3.1. `touch startPalavrasService`
3.2. Script
```
    #! /bin/bash
    export PYTHONPATH=$PYTHONPATH:root/palavrashttpendpoint/
    python3 root/palavrashttpendpoint/main/Main.py
```

4. Instalar o `pip3`
4.1. `sudo apt-get install python3-pip`
4.2. `pip3 install --upgrade pip` 

4. Instalar o modulo `flask` para o python3
4.1. `pip3 install flask`

5. Baixar o repostiróio no diretório `root`
5.1. `git clone https://alencarrh@bitbucket.org/enseproteam/palavrashttpendpoint.git`

6. Run `./root/startPalavrasService`

Observações:
Os caminhos estão fixos, verificar se estão de acordo com as configurações e locais do seu sistema operacional.

 
## Chamada 
 
```
http://127.0.0.1:8091/palavras/analisar?frase=Qua é a idade de Alencar?
```
 
## Retorno 
 
```
[
    {
        "numero": 0,
        "nivel": "0",
        "palavraOriginal": "",
        "palavraCanonica": "",
        "tags": [],
        "tagInicial": "QUE:fcl"
    },
    {
        "numero": 1,
        "nivel": "1",
        "palavraOriginal": "Qua",
        "palavraCanonica": "qua",
        "tags": [
            "<*>"
        ],
        "tagInicial": "fA:prp"
    },
    {
        "numero": 2,
        "nivel": "1",
        "palavraOriginal": "\u00e9",
        "palavraCanonica": "ser",
        "tags": [
            "",
            "",
            "",
            "PR",
            "3S",
            "IND",
            "VFIN"
        ],
        "tagInicial": "P:v-fin"
    },
    {
        "numero": 3,
        "nivel": "1",
        "palavraOriginal": "",
        "palavraCanonica": "",
        "tags": [],
        "tagInicial": "Cs:np"
    },
    {
        "numero": 4,
        "nivel": "2",
        "palavraOriginal": "a",
        "palavraCanonica": "o",
        "tags": [
            "",
            "F",
            "S"
        ],
        "tagInicial": "DN:art"
    },
    {
        "numero": 5,
        "nivel": "2",
        "palavraOriginal": "idade",
        "palavraCanonica": "idade",
        "tags": [
            "",
            "",
            "F",
            "S"
        ],
        "tagInicial": "H:n"
    },
    {
        "numero": 6,
        "nivel": "2",
        "palavraOriginal": "",
        "palavraCanonica": "",
        "tags": [],
        "tagInicial": "DN:pp"
    },
    {
        "numero": 7,
        "nivel": "3",
        "palavraOriginal": "de",
        "palavraCanonica": "de",
        "tags": [
            ""
        ],
        "tagInicial": "H:prp"
    },
    {
        "numero": 8,
        "nivel": "3",
        "palavraOriginal": "Alencar",
        "palavraCanonica": "Alencar",
        "tags": [
            "",
            "<*>",
            "M",
            "S"
        ],
        "tagInicial": "DP:prop"
    },
    {
        "numero": 9,
        "nivel": "1",
        "palavraOriginal": "",
        "palavraCanonica": "",
        "tags": [],
        "tagInicial": "?"
    }
]
```