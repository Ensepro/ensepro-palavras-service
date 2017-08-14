# Palavras Service 
 
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