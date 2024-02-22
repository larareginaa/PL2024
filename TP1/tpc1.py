import re
from collections import defaultdict



def processar_dados(linhas):

    modalidades = set()
    resultados = {'aptos': 0, 'inaptos': 0}
    escaloes = defaultdict(int)

    for linha in linhas[1:]:
        
        elementos = linha.split(",")

        idade = elementos[5].strip()
        modalidade = elementos[8].strip()
        resultado = elementos[12].strip()
        
        modalidades.add(modalidade)

        if resultado == 'true': resultados['aptos'] += 1
        else: resultados['inaptos'] += 1

        escalao = int(idade) // 5
        faixa = f"[{escalao*5}-{escalao*5+4}]"
        escaloes[faixa] += 1

    return modalidades, resultados, escaloes


def imprimir_outputs(modalidades, resultados, escaloes):

    print("1) Lista ordenada alfabeticamente das modalidades desportivas:")
    print(sorted(modalidades))

    print("\n2) Percentagens de atletas aptos e inaptos para a prática desportiva:")
    total = resultados['aptos'] + resultados['inaptos']
    print(f"Aptos: ", resultados['aptos'] / total * 100, "%")
    print(f"Inaptos: ", resultados['inaptos'] / total * 100, "%")

    print("\n3) Distribuição de atletas por escalão etário:")
    for chave, valor in escaloes.items():
        print(f"{chave}: {valor}")

    

if __name__ == "__main__":

    with open('emd.csv', 'r') as f:

        modalidades, resultados, escaloes = processar_dados(f.readlines())
        imprimir_outputs(modalidades, resultados, escaloes)
