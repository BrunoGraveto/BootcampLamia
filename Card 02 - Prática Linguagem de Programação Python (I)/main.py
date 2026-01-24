#!python3

print('Bem vindo Bruno!')

print('-> main.py: (esse)')
print(__name__)
print(__package__)

print('-> arquivo.py:')
import pacote.sub.arquivo

print('-> comentarios.py:')
from tipos import comentarios # Outro jeito para importar classes/arquivos

print('-> variaveis.py:')
from tipos import variaveis

print('-> basicos.py:')
from tipos import basicos

print('-> listas.py:')
import tipos.listas

print('-> tuplas.py:')
from tipos import tuplas

print('-> conjuntos.py')
import tipos.conjuntos

print('-> dicionarios.py')
import tipos.dicionarios

print('-> unarios.py')
import operadores.unarios

print('-> aritmeticos.py')
import operadores.aritmeticos

print('-> relacionais.py')
import operadores.relacionais

print('-> atribuicao.py')
from operadores import atribuicoes

print('-> ternarios.py')
from operadores import ternarios

print('-> if_1.py')
from controle import if_1

print('-> if_2.py')
from controle import if_2

print('-> for_1.py')
from controle import for_1

print('-> while_1.py')
from controle import while_1

print('-> outros_exemplos.py')
from controle import outros_exemplos