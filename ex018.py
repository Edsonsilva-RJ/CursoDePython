'''Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.'''
from math import sin, cos, tan, radians

ângulo = float(input('Digite o valor do ângulo qu você deseja: '))
seno = sin(radians(ângulo))
print('O angulo de {} tem o Seno de {:.2f}'. format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o Cosseno de {:.2f}'. format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O angulo de {} tem a Tangente de  {:.2f}'. format(ângulo, tangente))