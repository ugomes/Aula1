import pandas as pd

data = {
    'Nome': ['Uelton', 'Ana', 'Jéssica', 'Paulo', 'Henrique', 'João', 'José'],
    'Idade': [30, 25, 35, 28, 40, 22, 33],
    'Cidade': ['Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo', 'Manaus']
}


df = pd.DataFrame(data)


moradores_recife = df[df['Cidade'] == 'Recife']


print(moradores_recife)
