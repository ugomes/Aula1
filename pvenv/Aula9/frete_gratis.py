import requests # importação da biblioteca request

def obter_estado(cep):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")  # função para verificar o cep , estou fazendo um requisição no método GET e utlizando a API da VIACEP
    data = response.json() # obtendo os daods do Json
    if "erro" not in data: # tratando o erro, se o cep não for encontrado
        return data.get("uf") # retornado o estado 
    else:
        print("CEP não encontrado.")
        return None

def verificar_regiao(estado):
   
    estados_norte_nordeste = ["AC", "AL", "AM", "AP", "BA", "CE", "MA", "PA", "PB", "PE", "PI", "RN", "RO", "RR", "SE", "TO"] # Lista com os estados do Norte e Nordeste
    
    return estado in estados_norte_nordeste # Percorre a lista 


cep = input("Por favor, insira o CEP: ") # usuário insere o CEP

estado = obter_estado(cep) # verifica qual é o estadp 
if estado:
    if verificar_regiao(estado): # condições para verificar se o frete é grátis 
        print("O CEP é elegível para frete grátis.")
    else:
        print("O CEP não é elegível para frete grátis.")
