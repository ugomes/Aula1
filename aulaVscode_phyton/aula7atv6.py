#Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.

#Implementem uma função que receba uma palavra qualquer (string) como entrada.
#O programa deve imprimir o número total de vogais na palavra.
#Solicitação de Entrada:

#Implementem a solicitação de entrada de uma palavra (string).
#Contagem de Vogais:

#Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
#Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
#Imprima o número total de vogais na palavra.

palavra = input('Digite sua palavra: ')
vogais = 'aeiououAEIOUáéíóúàèìòùÁÉÍÓÚÀÈÌÒÙ'

contador_vogais = 0

for i in palavra:
    if i in vogais:
     contador_vogais += 1

print(f'A palavra {palavra} contém {contador_vogais} vogal(is)')


