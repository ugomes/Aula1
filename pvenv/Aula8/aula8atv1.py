import requests

squad ={
    'Agatha Salles': '05782360',
    'Elenice Damitz': '90620250',
    'Uelton Gomes': '08696470'
} # aqui cria o dicionário

for name, cep in squad.items(): # criando estrutura de repetição
    url = f'https://viacep.com.br/ws/{cep}/json/' # criando uma variável para a url
    response = requests.get(url) # obter a resposata da url
    data = response.json() # obter o arquivo json
    
    print(f'{name} - {data["logradouro"]}, {data["bairro"]}, {data["localidade"]}, {data["uf"]}') # printar na tela os resultados