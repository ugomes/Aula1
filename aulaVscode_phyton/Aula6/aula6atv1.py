#Construa um script para verificar se o usuário tem uma idade maior que 18 anos, se tiver, imprima na tela "Indivíduo possui idade mínima para dirigir"

idade = int(input(('Digite sua idade : ')))
 
if idade > 18:
  print('Indivíduo possui idade para dirigir')

elif idade == 18 or idade <= 17:  
 print("Indivíduo tem entre 17 e 18 anos e ainda NÂO está apto para dirigir ")
else:
  print('Indivíduo não possui idade para dirigir')
1