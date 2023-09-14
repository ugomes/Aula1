from faker import Faker


fake = Faker()


persona = {
    'Nome': fake.name(),
    'Idade': fake.random_int(min=18, max=70),
    'Profissão': fake.job(),
    'Localização': fake.city(),
    'Interesses': ', '.join(fake.words(nb=3, ext_word_list=None)),
    'Desafio': fake.sentence(),
    'Citação Favorita': fake.sentence(),
}


print("Persona:")
for chave, valor in persona.items():
    print(f"{chave}: {valor}")
