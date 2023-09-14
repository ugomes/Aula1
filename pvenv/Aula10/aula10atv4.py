from faker import Faker
import random


fake = Faker("pt_Br")


nome = fake.name()
idade = random.randint(18, 70)  
cidade = fake.city()


print("Persona:")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")
