### **TPC6**: Gramática Independente de Contexto
### **Autor**: Lara Regina da Silva Pereira, A100556

------------------------------------------------------------------------------

# Enunciado

O objetivo deste trabalho prático foi construir uma gramática independente de contexto de modo a representar expressões aritméticas e lógicas simples. A gramática é definida por um conjunto de terminais, não-terminais e produções que descrevem como as expressões podem ser formadas.

### Exemplos

```
?a
b=a*2/(27-3)
!a+b
c=(a*b)/(a/b)
```

------------------------------------------------------------------------------

# Proposta de resolução

```
T = {'?', '!', '(', ')', '=', '*', '/', '-', '+', var, num}

N = {S, Expr, Expr2, Expr3, Op, Op2}

S = S

P = {
    S -> '?' var            LA = {'?'}
       | '!' Expr           LA = {'!'}
       | var '=' Expr       LA = {var}

    Expr -> Expr2 Op

    Op -> '+' Expr          LA = {'+'}
        | '-' Expr          LA = {'-'}
        | &                 LA = {$, ')'}

    Expr2 -> Expr3 Op2      LA = {'(', var, num}

    Op2 -> '*' Expr         LA = {'*'}
         | '/' Expr         LA = {'/'}
         | &                LA = {'+', '-', $, ')'}

    Expr3 -> '(' Expr ')'   LA = {'('}
           | var            LA = {var}
           | num            LA = {num}
}
```
