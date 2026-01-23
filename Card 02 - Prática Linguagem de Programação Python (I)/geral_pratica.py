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
# UNARIOS

# ARITMÉTICOS

# RELACIONAIS