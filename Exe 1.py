def media_aluno(notas):
    soma = 0
    for i in notas:
        soma += i
    
    media = soma / len(notas)
    
    return media    
    
def notas_aluno():
    notas = []
    sim = "sim"

    while sim == "sim":
        notas.append(float(input("Digite sua nota: ")))
        sim = input("Deseja continuar colocando mais notas (sim/nao): ")
        
        if sim == "nao":
            break
    
    return notas

notas = notas_aluno()
media = media_aluno(notas)

print("A media das suas notas é: ", media,"pontos")
