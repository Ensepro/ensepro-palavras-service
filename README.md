# Palavras Service 
 
 
 Este README está desatualizado. Atualizarei assim que possível.
 
 
## Dependências

1. Python 3
2. Modulo `flask` (para instalar: `pip install flask`)

## Configurando serviço do zero

1. Criar o container a partir da imagem do Palavras.

```
docker run -it --name palavras_service -p 8099:8099 ubuntu/palavras:11952a /bin/bash
``` 

2. Criar o arquivo `palavrasTree` no diretório `root`
	1. `touch palavrasTree`
	2. Script
```
    #! /bin/bash
    export LANG=pt_BR.UTF-8
    export PERL_UNICODE=SDA
    echo $1 | /opt/palavras/por.pl | /opt/palavras/bin/dep2tree
```

3. Criar o arquivo `startPalavrasService` no diretório `root`
	1. `touch startPalavrasService`
	2. Script
```
    #! /bin/bash
    export PYTHONPATH=$PYTHONPATH:root/palavrashttpendpoint/
    python3 root/palavrashttpendpoint/main/Main.py
```

4. Instalar o `pip3`
	1. `sudo apt-get install python3-pip`
	2. `pip3 install --upgrade pip` 

5. Instalar o modulo `flask` para o python3
	1. `pip3 install flask`

6. Baixar o repostiróio no diretório `root`
	1. `git clone https://alencarrh@bitbucket.org/enseproteam/palavrashttpendpoint.git`

7. Run `./root/startPalavrasService`



##### Observações
Os caminhos estão fixos, verificar se estão de acordo com as configurações e locais do seu sistema operacional.


 
## Chamada 
 
```
http://127.0.0.1:8099/palavras/analisar?frase=Qua é a idade de Alencar?
```
 
## Retorno 
 
```
[
    {
        "numero": 0,
        "nivel": "0",
        "palavra_original": "",
        "palavra_canonica": "",
        "tags": [],
        "tag_inicial": "QUE:fcl"
    },
    {
        "numero": 1,
        "nivel": "1",
        "palavra_original": "Qua",
        "palavra_canonica": "qua",
        "tags": [
            "<*>"
        ],
        "tag_inicial": "fA:prp"
    },
    {
        "numero": 2,
        "nivel": "1",
        "palavra_original": "\u00e9",
        "palavra_canonica": "ser",
        "tags": [
            "",
            "",
            "",
            "PR",
            "3S",
            "IND",
            "VFIN"
        ],
        "tag_inicial": "P:v-fin"
    },
    {
        "numero": 3,
        "nivel": "1",
        "palavra_original": "",
        "palavra_canonica": "",
        "tags": [],
        "tag_inicial": "Cs:np"
    },
    {
        "numero": 4,
        "nivel": "2",
        "palavra_original": "a",
        "palavra_canonica": "o",
        "tags": [
            "",
            "F",
            "S"
        ],
        "tag_inicial": "DN:art"
    },
    {
        "numero": 5,
        "nivel": "2",
        "palavra_original": "idade",
        "palavra_canonica": "idade",
        "tags": [
            "",
            "",
            "F",
            "S"
        ],
        "tag_inicial": "H:n"
    },
    {
        "numero": 6,
        "nivel": "2",
        "palavra_original": "",
        "palavra_canonica": "",
        "tags": [],
        "tag_inicial": "DN:pp"
    },
    {
        "numero": 7,
        "nivel": "3",
        "palavra_original": "de",
        "palavra_canonica": "de",
        "tags": [
            ""
        ],
        "tag_inicial": "H:prp"
    },
    {
        "numero": 8,
        "nivel": "3",
        "palavra_original": "Alencar",
        "palavra_canonica": "Alencar",
        "tags": [
            "",
            "<*>",
            "M",
            "S"
        ],
        "tag_inicial": "DP:prop"
    },
    {
        "numero": 9,
        "nivel": "1",
        "palavra_original": "",
        "palavra_canonica": "",
        "tags": [],
        "tag_inicial": "?"
    }
]
```
