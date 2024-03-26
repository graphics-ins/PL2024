# TPC5: Gramática Independente de Contexto
## 2024-03-26
## Autor:
A95458

Inês Meneses de Castro

## Resumo

Construir uma gramática para uma linguagem simples do tipo:

```
?a 
b=a*2/(27-3)
!a+b
c=a*b/(a/b)
```
## Resolução

```
T =  {'?', var, '=', '*', num, '/', '(', '-', ')', '+', '!'}

N = {S, Exp1, Exp2, Exp3, Op1, Op2}

S = S

P = {

    S -> '?' var               LA = {'?'}
        |'!' Expr              LA = {'!'}
        |var '=' Expr          LA = {var}

    Expr -> Exp2 Op        

    Op  -> '+' Expr            LA = {'+'}
        | '-' Expr             LA = {'-'}
        | &                    LA = Follow(Op) = Follow(Expr) = {')'}

    Exp2 -> Expr3 Op2       

    Op2 -> '*' Expr            LA = {'*'}
          | '/' Expr           LA = {'/'}
          | &                  LA = Follow(Op2) = Follow(Expr2) = {')','+','-'}

    Expr3 -> '(' Exp1 ')'      LA = {'('}
            | num              LA = {num}
            | var              LA = {var}

}
```
