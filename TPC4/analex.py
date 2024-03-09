import ply.lex as lex


tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'IDENTIFIER',
    'COMMA',
    'GREATER_EQUAL',
    'NUMBER'
)

t_SELECT = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_FROM = r'[fF][Rr][Oo][Mm]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_GREATER_EQUAL = r'>='
t_COMMA = r','

t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    t.type = 'NUMBER'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'  
    return t

def t_error(t):
    print("Caracter inválido: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()



query = "Select id, nome, salario From empregados Where salario >= 820"

lexer.input(query)
for token in lexer:
    print(token)
