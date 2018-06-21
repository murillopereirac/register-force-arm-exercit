#!/usr/bin/python
#Exercicio aula 3 - Operadores Logicos IF ELSE em python3

print('Cadastro Nacional para as Forças Armadas do Exercito')

nome = input('Escreva seu nome: ')
idade = int(input('Escreva sua idade: '))
peso = float(input('Escreva seu peso: '))
altura = float(input('Escreva sua altura: '))

if idade >= 18:
    print('Voce tem a idade ideal para engressar nas Forças Armadas.')
elif idade < 18:
    print('Voce nao tem a idade suficiente para engressar nas Forças Armadas.')
if peso >= 60:
    print('Voce esta no peso ideal para engressar nas Forças Armadas.')
elif peso < 60:
    print('Voce esta com o peso abaixo do exigido para engressar nas Forças Armadas.')
if altura >= 1.70:
    print('Voce tem a altura ideal para engressar nas Forças Armadas.')
elif altura < 1.70:
    print('Voce nao tem a altura adequada para engressar nas Forças Armadas.')
if idade >= 18 and peso >= 60 and altura >= 1.70:
    print(nome, 'voce tem os requisitos para engressar nas Forças Armadas!')
elif  idade < 18 and peso < 60 and altura < 1.70:
    print(nome, 'voce nao tem os requisitos exigidos para engressar nas Forças Armadas!')