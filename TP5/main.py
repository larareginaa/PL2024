import json
from datetime import datetime
import ply.lex as lex


moedas_aceites = [1, 2, 5, 10, 20, 50, 100, 200]

reserved = {
    "listar": "LISTAR",
    "moeda": "MOEDA",
    "selecionar": "SELECIONAR",
    "sair": "SAIR",
}

tokens = [
    "COMMAND",
    "MONEY",
    "EUR",
    "CENT",
    "POSITION"
] + list(reserved.values())

t_POSITION = r'[A-Z]\d+'


def t_MONEY(t):
    r'\d+[e|c]'
    if saldo_para_cents(t.value) not in moedas_aceites:
        raise ValueError(f"Moeda não aceite: {t.value}")
    if "e" in t.value:
        t.type = "EUR"
    elif "c" in t.value:
        t.type = "CENT"
    return t


def t_COMMAND(t):
    r'\b[a-z|A-Z]+\b'
    t.type = reserved.get(t.value.lower(), "COMMAND")
    return t


t_ignore = ' ,.'


def t_error(t):
    raise ValueError(f"Valor inválido: {t.value}")


def listar(stock):
    print("""
cod | nome             | quantidade | preço
-------------------------------------------""")
    for product in stock:
        spaces_n = " " * (16 - len(product['nome']))
        spaces_q = " " * (10 - len(str(product['quant'])))
        print(
            f"{product['cod']} | {product['nome']}{spaces_n} | {product['quant']}{spaces_q} | {product['preco']}")


def cents_para_saldo(cents):
    euros = cents // 100
    centimos = cents % 100
    return f"{euros}e{centimos}c"


def saldo_para_cents(saldo):
    if "e" in saldo and "c" in saldo:
        saldo = saldo.replace("e", ".")
        saldo = saldo.replace("c", "")
        saldo = saldo.split(".")
        return int(saldo[0]) * 100 + int(saldo[1])
    elif "e" in saldo:
        saldo = saldo.split("e")
        return int(saldo[0]) * 100
    else:
        saldo = saldo.split("c")
        return int(saldo[0])


def tokenizar(texto):
    res = []

    # build the lexer
    lexer = lex.lex()
    lexer.input(texto)
    # tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
        res.append(tok)

    return res


def moeda(tokens):
    cents = 0
    for t in tokens[1:]:
        if t.type == "EUR" or t.type == "CENT":
            cents += saldo_para_cents(t.value)
    return cents


def selecionar(tokens, stock, cents):
    posicao = tokens[1].value

    for product in stock:
        if product['cod'] == posicao and product['quant'] > 0:
            if product['preco'] <= cents:
                product['quant'] -= 1
                return product
            else:
                raise ValueError(
                    f"Saldo insuficiente para comprar '{product['nome']}': {product['preco']}")

    raise ValueError(
        f"Produto esgotado ou não encontrado na posição {posicao}")


def print_saldo(cents):
    print(f"maq: Saldo = {cents_para_saldo(cents)}")


def main():
    stock = {}
    with open("stock.json") as file:
        stock = json.load(file)

    print(
        f"maq: {datetime.now().strftime('%Y-%m-%d')}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    cents = 0

    leave = False
    while not leave:
        try:
            tokens = tokenizar(input(">> "))
            command = tokens[0].value.upper()
            if command == "LISTAR":
                listar(stock)
            elif command == "MOEDA":
                cents += moeda(tokens)
                print_saldo(cents)
            elif command == "SELECIONAR":
                try:
                    product = selecionar(tokens, stock, cents)
                    print(
                        f"maq: Pode retirar o produto dispensado '{product['nome']}'")
                    cents -= int(product['preco'] * 100)
                    print_saldo(cents)
                except ValueError as e:
                    print(f"maq: {e}")
                    print_saldo(cents)
            elif command == "SAIR":
                print(f"maq: Pode retirar o troco: {cents_para_saldo(cents)}")
                print("maq: Até à próxima")
                leave = True
            else:
                print("maq: Comando inválido. Tente novamente.")
        except ValueError as e:
            print(f"maq: {e}")


main()
