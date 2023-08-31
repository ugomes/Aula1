print(145+234)


loja = 'ROUPAS SA'
clientes = "200"
nome = "PAULA MARTINS"
mes = "JANEIRO"
valor = "R$500"
desconto = "10"
cupom = 'PAULA'

print('A loja tem ' + clientes + ' clientes e quer enviar mensagens nominais a cada um. A mensagem seria a seguinte:');
mensagem = ('Olá ' + nome + '. Em ' + mes + ', você realizou uma compra no valor de ' + valor + ' e ganhou um desconto de ' + desconto + ' %em sua próxima compra. Use o cupom ' + cupom + 'É'+desconto);
print (mensagem)

## Exemplo da aula input, str, int 

nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
mes = 'JANEIRO'
n1 = int(input('Digite o sua 1 nota: '))
n2 = int(input('Digite o sua 2 nota: '))
# desconto = int('10')
# cupom = nome + "É" + desconto
# tipo_nome = type(desconto)
# print(tipo_nome)
soma = n1 + n2 

print(f" O nome é: {nome} {sobrenome} a primeira nota é {n1} e a segunda é {n2} a minha nota geral é {soma}")