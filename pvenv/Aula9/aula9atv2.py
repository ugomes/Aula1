
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def obter_matricula_valida():
    while True:
        entrada = input("Digite um número de matrícula (ou '0' para parar): ")
        if entrada == '0':
            return None  
        elif entrada.isdigit():
            return int(entrada)  
        else:
            print("Por favor, insira um número válido.")

matriculas = []


for _ in range(5):
    matricula = obter_matricula_valida()
    if matricula is None:
        break  
    matriculas.append(matricula)


if not matriculas:
    print("Nenhum número de matrícula foi inserido.")
else:
    
    for matricula in matriculas:
        resultado = verificar_par_ou_impar(matricula)
        print(f"Matrícula {matricula} é {resultado}.")

        resultado = verificar_par_ou_impar(matricula)
        print(f"Matrícula {matricula} é {resultado}.")



