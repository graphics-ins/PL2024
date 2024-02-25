import re
import sys

def somador(texto):
    somar = True
    soma_total = 0

    regex_numeros = r'[-+]\d+'
    regex_on_off = re.compile(r'(ON|OFF)', re.IGNORECASE)
    regex_solucao = re.compile(r'=')

    delimitador_regex =  r'(?P<numeros>\d+)|(?P<liga>[Oo][Nn])|(?P<desliga>[Oo][Ff]{2})|(?P<resultado>=)'

    # Dividindo o texto em blocos delimitados por pares de instruções "ON" e "OFF"
    blocos = re.finditer(delimitador_regex, texto)

    for bloco in blocos:

        # Se a instrução "ON" estiver presente, somar os números no bloco
            if bloco.lastgroup == 'liga':
                somar = True

            elif bloco.lastgroup == 'desliga':
                somar = False

            elif bloco.lastgroup == 'resultado':
                print(soma_total)

            elif somar:
                x = int(bloco.group('numeros'))
                soma_total += x

    return soma_total


if __name__ == '__main__':

    texto_exemplo = "ON Começamos com 10, ON depois mais 5, OFF e então = mais 8. ON E por fim, 15. OFF"
    texto_exemplo2 = "ONsdgfsjk10hdbjzhhs4OFFsjkhd8 sahgd/$/%(()&="
    print(somador(texto_exemplo2))
