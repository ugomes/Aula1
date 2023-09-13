def calcular_preco_total(valor_total, desconto_percental): # Começa com def depois colocamos o nome da função o que está dentro de parenteses são os parametros que vamos passar
    desconto = valor_total * (desconto_percental/100) # Cálculo para encontrar o desconto
    preco_com_desconto = valor_total - desconto # Cálculo para temos o valor do preco com desconto
    return preco_com_desconto # Returno do valor, ou seja, a função precisa retornar o valor que queremos, sempre que queremos que returne um valor usamos o return
    
valor_da_compra = 100 #variável com  o valor da compra
desconto_oferecido = 10 # variável com desconto

preco_final = calcular_preco_total(valor_da_compra,desconto_oferecido) # variável  para encontrar o preço final, note que estamos chamando a função, ou seja o programa  executa a função realiza o cálculo  do preço com desconto, 
                                                                       # dentro dos parenteses são os parâmetros, que foram nossas vaiáveis declaradas lá em cima
                                                                       
                                                              

                                                            

print("Preço Total após o desconto: R$",preco_final) # printando o valor final