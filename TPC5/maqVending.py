import ply.lex as lex
import csv
import sys

saldo = 0
saldo_atual = 0
apagar = 0
produtos = {}

with open('produtos.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                produtos[lines[0]] = lines[1],lines[2]

tokens = (
    'ID',
    'MOEDA',
    'LISTAR',
    'SELECIONAR',
    'SAIR'
)

states = (
        ('selecionar','exclusive'),
        ('input','exclusive'),
    )

def parse_coin_value(coin_str):
    coin_values = {
        "5c": 5,
        "10c": 10,
        "20c": 20,
        "50c": 50,
        "1e": 100,
        "2e": 200
    }
    return coin_values[coin_str]

def t_input_MOEDA(t):
    r'5c|10c|20c|50c|1e|2e'
    global saldo_atual
    saldo_atual +=  parse_coin_value(t.value)
    print("SALDO = " + str(saldo_atual))
    return t

def t_input_LISTAR(t):
    r'[Ll][Ii][Ss][Tt][Aa][Rr]'
    for _id in produtos.keys():
            if _id == "id":
                pass
            else:
                tup = produtos[_id]
                print(f"{_id} {tup[0]} {tup[1]}")
    return t

def t_selecionar_ID(t):
    r'\d+'
    preco = produtos[t.value][1]
    split = preco.split('c')
    global apagar
    apagar += int(split[0])
    lexer.begin('input')
    return t

def t_input_SELECIONAR(t):
    r'[Ss][Ee][Ll][Ee][Cc][Ii][Oo][Nn][Aa][Rr]'
    lexer.begin('selecionar')
    return t

def t_input_SAIR(t):
    r'[Ss][Aa][Ii][Rr]'
    global troco, saldo_atual, apagar
    troco = saldo_atual - apagar
    if troco<0:
         print("Introduza o dinheiro!")
    else:
        global saldo 
        saldo = saldo + apagar
        print("TROCO = " + str(troco))
        troco = 0
        saldo_atual = 0
    return t





def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore = " \t"

def t_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)



lexer = lex.lex()
lexer.begin('receber')

lexer.input(""" MOEDA 1e 
                MOEDA 10c 
                MOEDA 20c
                LISTAR
                SELECIONAR 2
                SAIR
            """)



for line in sys.stdin:
    lexer.input(line)
    t = True
    while t == True:
        tok = lexer.token()
        if not tok: 
            t = False   



