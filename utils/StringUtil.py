
import unicodedata


def isEmpty(string):
    return (string is None or string == '' or string.replace(" ", "") == '')


def removeStrings(strings, fromString, toString):
    for string in strings:
        fromString = fromString.replace(string, toString)
    return fromString


def removeAcentuacao(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

#TODO: comentar e renomear variáveis
def find(a, b):
    for i in range(len(a)):
        if(b == a[i]):
            return i
    return -1