#Crie um script com as seguintes instruções, pesquisando na internet como fazer:
# Crie uma tupla com 5 dados
# Altere a tupla para uma lista
# Insira 2 dados extras a essa lista
# Remova o primeiro dado da lista
# Remova o último dado da lista
# Faça um print com o primeiro dado da lista
# Faça um print com a quantidade de dados da lista
# Crie um dicionário com os seguintes dados:
# Nome, Idade, Profissão
#Imprima somente o valor contido na chave Nome do dicionário


#1: Crie uma tupla com 5 dados
times_de_futebol = ("Flamengo", "Palmeiras", "São Paulo", "Grêmio", "Internacional")

#2: Altere a tupla para uma lista
lista_times_de_futebol = list(times_de_futebol)

#3: Insira 2 dados extras a essa lista
lista_times_de_futebol.append("Atlético-MG")
lista_times_de_futebol.append("Santos")
lista_times_de_futebol.append("Corinthians")  

#4: Remova o primeiro dado da lista (Flamengo)
lista_times_de_futebol.remove("Flamengo")

#5: Remova um dado específico da lista (Santos)
lista_times_de_futebol.remove("Santos")

#6: Faça um print com o primeiro dado da lista
print(lista_times_de_futebol[0])

#7: Faça um print com a quantidade de dados da lista
print(len(lista_times_de_futebol))

# Passo 8: Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
meu_dicionario = {
    "Nome": "João",
    "Idade": 30,
    "Profissão": "Engenheiro"
}

# Passo 9: Imprima somente o valor contido na chave Nome do dicionário
print(meu_dicionario["Nome"])
