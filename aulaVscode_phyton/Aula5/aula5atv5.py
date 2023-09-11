##Desafio: Fazer um programa que some 4 notas e, no final, tenha a média aritmética dessas notas.

##O que seu programa deve conter:

##Um input onde cada interação tenha um texto.
##No final, seu programa deverá ter o output:
## “Olá, Caique! Sua média é: 10 pontos”

print(' Olá aluno para saber as médias  das suas notas, digite suas notas abaixo:')

nome = input('Digite seu nome: ')
nota1= int(input('Digite sua primeira nota: '))
nota2= int(input('Digite sua segunda nota: '))
nota3=int(input('Digite sua terceita nota: '))
media_notas = (nota1 + nota2 +nota3)/3


print(f' Olá, {nome} ! Sua média é:  {media_notas} pontos')

