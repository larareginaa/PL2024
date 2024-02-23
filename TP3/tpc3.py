import sys
import re


def somador(texto):

    somador = True
    resultado = 0

    for sequencia in re.split(r'=', texto)[:-1]:

        for elemento in re.findall(r'\d+|on|off', sequencia, flags=re.IGNORECASE | re.MULTILINE):

            if re.match(r'on', elemento, flags=re.IGNORECASE): somador = True
            elif re.match(r'off', elemento, flags=re.IGNORECASE): somador = False

            elif somador: resultado += sum([int(e) for e in re.findall(r'\d', elemento)])

        print(resultado)



if __name__ == "__main__":

    with open(sys.argv[1], 'r') as f: somador(f.read())
