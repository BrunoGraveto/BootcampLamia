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

# TERNARIO: "Três partes"
temBrilho = True

        # "1 parte"    # "2 parte"         # "3 parte"
fala = 'É uma jóia!' if temBrilho else 'Vix, é só uma pedra!'
print(fala)

idade = 19
maiorIdade = True if idade >= 18 else False
print(f'É maior de idade? {maiorIdade}')

# CONDIÇÃO: "IF"
alunoComportado = True

if alunoComportado:
    print('Muito bem, continue assim!')
else:
    print('Aí não dá né meu caro, melhora ai...')
    
idade = int(input('Digite sua idade: '))

if idade <= 8:
    print('Criança!')
elif idade <= 12:
    print('Pré-adolescente!')
elif idade <= 18:
    print('Adolescente!')
elif idade <= 50:
    print('Adulto!')
else:
    print('Idoso!')
    
# LOOPS: FOR
print('Contando até 10:')
for i in range(10):
    print(i, end=' ')
    
print('')
    
print('Contando de 1 até 10:')
for i in range(1, 11):
    print(i, end=' ')

print('')
    
print('Contando de 1 até 10 em 2 em 2:')
for i in range(1, 11, 2):
    print(i, end=' ')

print('')

alunos = ['Bruno', 'Igor', 'Jefferson', 'Marciano']
print('Lista de Alunos:')
for aluno in alunos:
    print(aluno)
    
nums = {1, 1, 2, 2, 3, 3}
print('Números de um conjunto:')
for num in nums:
    print(num)
    
moto = {
    'modelo': 'CG TITAN',
    'cilindrada': '160',
    'ano': '2019'
}

print('Características da Moto:')
for atrib in moto:
    print(atrib, ': ', moto[atrib])
    
print('\nCaracterísticas da Moto: [2]')
for atrib, valor in moto.items():
    print(atrib, ': ', valor)
    
print('\nAtributos da Moto:')
for atrib in moto.keys():
    print(atrib)
    
print('\nValores da Moto:')
for valor in moto.values():
    print(valor)
    
# LOOPS: WHILE
print('A bomba vai explodir em...')
tempo = 10

while tempo > 0:
    print(f'Explodindo em {tempo}...')
    tempo -= 1

print('BOOOOOOMMMM')

print('\nAté você não digitar \"sair\" você não sai daqui!')

texto = ""

while(texto != 'sair'):
    texto = input('Digite:')

print('Você saiu!')