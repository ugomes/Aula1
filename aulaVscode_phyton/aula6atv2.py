#EM SQUADS

#Leiam o texto abaixo e resolvam.

#Na "FashionStyle", para um cliente obter 10% de desconto em suas compras, a compra deve ser de pelo menos R$250,00 e para obter 30%, a compra deve ser acima de R$500,00. Caso contrário, nenhum desconto é aplicado.

#No caixa, haverá uma tela voltada para o cliente. Ao passar o produto, caso cumpra o requisito da promoção, aparecerá a mensagem:

#Caso o cliente não cumpra o requisito, deve aparecer "POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA."

#Caso o cliente faça uma compra acima de R$250,00 "PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00"

#Caso o cliente faça uma compra acima de R$500,00 "PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%"

valor_compra = int(input(('Digite o valor da sua compra: ')))
  
if valor_compra < 250:
    print('POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA')
elif valor_compra > 250 or valor_compra<= 500:
    print('PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00')   
elif valor_compra > 500: 
    print('PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%')  
