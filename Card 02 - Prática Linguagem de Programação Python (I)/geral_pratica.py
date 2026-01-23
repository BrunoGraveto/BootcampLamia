# Para criar comentários podemos utilizar tanto # quanto """

# Exemplo

"""
Exemplo
"""

# Para importar os arquivos podemos utilizar dois formatos:
import tipos.variaveis
from tipos import variaveis

## VARIAVEIS ##
"""
O Python é uma linguagem não tipada, portanto podemos declarar
varias variaveis apenas mudando o que atribuimos a elas:
"""
num = 1
nome = 'Josimar'
nota = 9.9

## PRINT ##

# Podemos ver os tipos de diferentes variaveis dessa forma:
print(type(nome)) # No caso, String

# Para printar uma variavel que não seja String podemos fazer:
print('Nota: ' + str(nota))

# Outra forma de print:
print(f'num: {num}')

## LISTAS ##

# Para criar:
lista = [1, 2, 3] 

# Para adicionar:
lista.append(5)

# Para trocar um determinado valor
lista[3] = 4

# Para inserir um determinado valor depois de um index
lista.insert(0, 0)

## TUPLAS ##
"""
Após a criação não é possivel adicionar
outros valores.
"""

# Para criar:
tupla = (1, 2, 3) 

# Para verificar se um determinado valor esta presente podemos:
estaNaTupla = 1 in tupla

## CONJUNTOS ##
# Não aceita repetições

# Para criar:
conjunto = {1, 2, 3} 

# Para adicionar:
conjunto.add(4)

## DICIONÁRIOS ##

# Para criar:
dicionario = {
    'lingua': 'Português',
    'autor': 'Bruno Alcantara',
    'Ano': 2026
}

# Para acessar um atributo:
print('Linguagem do dicionário: ' + dicionario['lingua'])

## OPERADORES ##
# UNARIOS: envolvem uma unica "condição"
var = not False
print(f'Meu nome é Bruno? {var}')

num = 3
num = -num
print(f'Negativo de 3 é {num}')

# ARITMÉTICOS: no caso, para cálculos
soma = 1 + 1
print(f'Soma de 1 + 1: {soma}')
sub = 1 - 1
print(f'Subtração de 1 - 1: {sub}')
mult = 1 * 1
print(f'Multiplicação de 1 * 1: {mult}')
div = 1 / 1
print(f'Divisão de 1 / 1: {div}')
resto = 1 % 1
print(f'Resto de 1 / 1 (1 % 1): {resto}')

# RELACIONAIS: comparação 
x = 10
y = 20

igual = x == y
print(f'X({x}) == Y({y}): {igual}')
dif = x != y
print(f'X({x}) != Y({y}): {dif}')
maior = x > y
print(f'X({x}) > Y({y}): {maior}')
menor = x < y
print(f'X({x}) < Y({y}): {menor}')

# ATRIBUIÇÃO: formas de "manipular" as variaveis
x = 0

# ADD
x += 1
print(f'Incremento em x: {x}')

# SUB
x -= 2
print(f'Decremento em x: {x}')

# MULT
x *= 5
print(f'Multiplicação em x: {x}')

# DIV
x /= 2
print(f'Divisão em x: {x}')

# RESTO
x %= 2
print(f'Módulo em x: {x}')

# LÓGICOS: definem "True" ou "False"
verdade = True
mentira = False

print(f'Verdade & verdade: {verdade and verdade}')
print(f'Mentira & mentira: {mentira and mentira}')
print(f'Verdade & mentira: {verdade and mentira}')

print(f'Verdade | verdade: {verdade or verdade}')
print(f'Mentira | mentira: {mentira or mentira}')
print(f'Verdade | mentira: {verdade or mentira}')

print(f'Verdade & NÃO verdade: {verdade and not verdade}')
print(f'NÃO Mentira | mentira: {not mentira or mentira}')

