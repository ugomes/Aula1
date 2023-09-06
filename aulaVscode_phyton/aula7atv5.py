while True:
    email = input('Insira seu e-mail: ')
 
    if '@jogajuntoinstituto.org' in email:
        print('Email Válido')
        break  # Sair do loop 
    else:
        print('Email inválido')


 # #Funcionalidade: Verificação de Email
 # Cenário: Inserção de email válido
 
 #  Dado que o usuário insere um email com o dominínio '@jogajuntoinstituto.org'
 #  Quando clica no botão ENTRAR
 # Então o sistema confirma que o e-mail é válido

 ## Funcionalidade: Verificação de Email
 # Cenário: Inserção de email inválido
 
 #  Dado que o usuário insere um email com o dominínio diferente de '@jogajuntoinstituto.org'
 #  Quando clica no botão ENTRAR
 # Então o sistema confirma que o e-mail é inválido
    