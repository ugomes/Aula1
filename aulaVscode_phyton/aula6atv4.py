#Na "Farmácia MINHA FARMA", clientes que comprarem produtos no valor total de R$ 100 ou mais ganham um vale-compras de R$ 10 para a próxima compra. Compras de valores menores não se qualificam para o vale.

#Ao conseguir atingir o limite mínimo da compra estabelecido na promoção, deve aparecer na nota fiscal "SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R$10 REAIS DE DESCONTO.".

#Caso o cliente não cumpra o requisito, deve aparecer "OBRIGADO POR ESCOLHER A MINHA FARMA. VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS GERAM UM VOUCHER DE R$10 REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?"

valor_compra = float(input(('Digite o valor da sua compra: R$ '))) # digitar o valor da compra 

if valor_compra >= 100:
  print('SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R$10 REAIS DE DESCONTO')

else:
   print('OBRIGADO POR ESCOLHER A MINHA FARMA. VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS GERAM UM VOUCHER DE R$10 REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?')  