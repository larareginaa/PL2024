import sys
import ply.lex as lex

reserved = {
    "select": "SELECT",
    "from": "FROM",
    "where": "WHERE",
}

tokens = [
   'ATTRIBUTE',
   'PLUS',
   'MINUS',
   'MULTIPLY',
   'DIVIDE',
   'MOREOREQUAL',
   'LESSOREQUAL',
   'MORE',
   'LESS',
   'NUMBER'
 ] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MOREOREQUAL = r'>='
t_LESSOREQUAL = r'<='
t_MORE = r'>'
t_LESS = r'<'

def t_ATTRIBUTE(t):
    r'\b[a-z|A-Z]+\b'
    t.type = reserved.get(t.value.lower(), "ATTRIBUTE")
    return t

def t_NUMBER(t):
    r'\d+[.]?\d*'
    if "." in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# track number of lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ignored characters (spaces and tabs)
t_ignore  = ' \t,;'

# error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()

def main(argv):
    if len(argv) < 2:
        return
    lexer.input(argv[1])
    # tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break
        print(tok)

if __name__ == "__main__":  
    main(sys.argv)
