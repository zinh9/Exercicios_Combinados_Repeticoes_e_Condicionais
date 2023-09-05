def numeros_usuario():
    numeros = []
    sim = "sim"

    while sim == "sim":
        numeros.append(float(input("Digite sua nota: ")))
        sim = input("Deseja continuar colocando mais notas (sim/nao): ")
        
        if sim == "nao":
            break
    
    return numeros
    
def menor_num(numeros):
    menor = numeros[0]
    
    for i in numeros:
        if i < menor:
            menor = i
    
    return menor

numeros = numeros_usuario()
menor = menor_num(numeros)

print("O menor numero digitado é: ", menor)
