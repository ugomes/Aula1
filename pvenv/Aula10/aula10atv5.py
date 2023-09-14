import pandas as pd
from faker import Faker
import random


def criar_persona():
    fake = Faker('pt_BR')  # Configurar o Faker para dados brasileiros
    nome = fake.name()
    idade = random.randint(18, 70)
    cidade = fake.city()
    return {'Nome': nome, 'Idade': idade, 'Cidade': cidade}


numumero_personas = 5  
personas = [criar_persona() for _ in range(numumero_personas)]


df = pd.DataFrame(personas)


df.to_csv('personas.csv', index=False)

print("Personas criadas e salvas em 'personas.csv'")
