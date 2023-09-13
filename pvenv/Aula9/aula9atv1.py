def determinar_cor_do_grupo(matricula):
    if matricula % 2 == 0:
        return "azul"
    else:
        return "amarelo" // Função


numero_matricula = int(input("Digite o número da matrícula: "))


cor_do_grupo = determinar_cor_do_grupo(numero_matricula)


print(f"VOCÊ ESTÁ NO TIME {cor_do_grupo.upper()}")
