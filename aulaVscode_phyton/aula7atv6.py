#Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.

#Implementem uma função que receba uma palavra qualquer (string) como entrada.
#O programa deve imprimir o número total de vogais na palavra.
#Solicitação de Entrada:

#Implementem a solicitação de entrada de uma palavra (string).
#Contagem de Vogais:

#Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
#Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
#Imprima o número total de vogais na palavra.

palavra = input('Digite sua palavra: ') #Aqui reserva a palavra digitada
vogais = 'aeiououAEIOUáéíóúàèìòùÁÉÍÓÚÀÈÌÒÙ' # Determinando as vogais como variáveis para conferência

contador_vogais = 0 # contador de vogais iniciando do zero

for vogal in palavra: # início de estrutuda de repetição - Aqui estou falando para ele percorrer a palavra digitada  e procurar a vogal
    if vogal in vogais: # se vogal estiver dentro de vogais
     contador_vogais += 1 # então comece a contar, acrescentando +1 a cada vogal encontrada 

print(f'A palavra {palavra} contém {contador_vogais} vogal(is)') # imprimir no console quantas vogais a palavra tem


