import random

print("Bem vindo ao jogo de adivinhação!!!\n\nNesse jogo você deve adivinhar/chutar qual numero o programa escolheu.\nVocê começa com o total de 100 pontos, a cada vez que você erra um numero você perde 10 pontos, e a cada dica vpcê perde 5 pontos.\n")

print("Ranking:\nDiamante: 100 pontos\nOuro: 75 pontos\nPrata: 50 pontos\nBronze: 25 pontos\nBarro: 0 pontos\n")

def jogo_multiplayer(num_aleatorio, jogador_1, jogador_2):
    chute_1 = []
    chute_2 = []
    pontos_1 = 100
    pontos_2 = 100
    i = 0
    
    dado = random.randint(1, 5)
    resposta_1 = int(input(jogador_1,", escolha um numero de 1 a 5: "))
    resposta_2 = int(input(jogador_2,", escolha um numero de 1 a 5: "))
        
    if resposta_1 == dado:
        print(jogador_1,"começa o jogo!")
        
        while i < 10:
            chute_1.append(int(input(jogador_1,", qual numero o programa escolheu: ")))
            
            if chute_1[i] != num_aleatorio:
                pontos_1 -= 10
                
                chute_2.append(int(input(jogador_2,", qual numero o programa escolheu: ")))
                
                if chute_2[i] != num_aleatorio:
                    pontos_2 -= 10
                
                elif chute_2[i] > num_aleatorio:
                    print("Um pouco menos")
            
                elif chute_2[i] < num_aleatorio:
                    print("Um pouco mais")
            
                elif chute_2[i] == num_aleatorio:
                    print("O", jogador_2,"ganhou o jogo com: ", len(chute_2),"chutes!!!")
            
            elif chute_1[i] > num_aleatorio:
                print("Um pouco menos")
            
            elif chute_1[i] < num_aleatorio:
                print("Um pouco mais")
            
            elif chute_1[i] == num_aleatorio:
                print("O", jogador_1,"ganhou o jogo com: ", len(chute_1),"chutes!!!")
            
            i += 1
    
    elif resposta_2 == dado:
        print(jogador_2,"começa o jogo!")
        
        while i < 10:
            chute_2.append(int(input(jogador_2,", qual numero o programa escolheu: ")))
            
            if chute_2[i] != num_aleatorio:
                pontos_2 -= 10
                
                chute_1.append(int(input(jogador_1,", qual numero o programa escolheu: ")))
                
                if chute_1[i] != num_aleatorio:
                    pontos_1 -= 10
                
                elif chute_1[i] > num_aleatorio:
                    print("Um pouco menos")
            
                elif chute_1[i] < num_aleatorio:
                    print("Um pouco mais")
            
                elif chute_1[i] == num_aleatorio:
                    print("O", jogador_1,"ganhou o jogo com: ", len(chute_1),"chutes!!!")
            
            elif chute_2[i] > num_aleatorio:
                print("Um pouco menos")
            
            elif chute_2[i] < num_aleatorio:
                print("Um pouco mais")
            
            elif chute_2[i] == num_aleatorio:
                print("O", jogador_2,"ganhou o jogo com: ", len(chute_2),"chutes!!!")
            
            i += 1
    
def resp_multiplayer(num_aleatorio):
    resposta = input("Deseja jogar modo multiplayer (sim/nao) ?: ")
    
    if resposta == "sim":
        jogador_1 = input("Digite o nome do jogador 1: ")
        jogador_2 = input("Digite o nome do jogador 2: ")
        
        jogo_multiplayer(num_aleatorio, jogador_1, jogador_2)
    
    else:
        return
    
def jogo(num_aleatorio):
    chute = []
    pontos = 100
    i = 0
    
    while i < 10:
        chute.append(int(input("Qual numero o programa escolheu: ")))
        
        if chute[i] != num_aleatorio:
            pontos -= 10
            
        if chute[i] == num_aleatorio:
            print("PARABÉNS!!! VOCÊ GANHOU O JOGO COM: ", len(chute),"CHUTES")
            
            ranking(pontos)
            
            break
        
        elif chute[i] > num_aleatorio:
            print("Um pouco menos")
        
        elif chute[i] < num_aleatorio:
            print("Um pouco mais")
        
        elif i < 10:
            print("Gamer Over")
            break
        
        if i == 3:
            resposta = input("Quer uma dica: ")
            
            if resposta == "sim":
                dica = dicas(i, num_aleatorio)
                pontos -= 5
                print(dica)
        
        i += 1

def dicas(i, num_aleatorio):
    dica = random.randint(1, 4)
    resultado = ""     
    
    if dica == 1 and num_aleatorio % 2 == 0:
        resultado = "O numero é par"
                
    elif dica == 2 and num_aleatorio % 2 == 1:
        resultado = "O numero é impar"
                
    elif dica == 3 and num_aleatorio > 50:
        resultado = "O numeros é maior que 50"
                
    elif dica == 4 and num_aleatorio < 50:
        resultado = "O numeros é menor que 50"
    
    return resultado

def ranking(pontos):
    if 75 < pontos <= 100:
        print("Seu ranking é: Diamante")
    
    elif 50 < pontos <= 75:
        print("Seu ranking é: Ouro")
    
    elif 25 < pontos <= 50:
        print("Seu ranking é: Prata")
    
    elif 15 < pontos <= 25:
        print("Seu ranking é: Bronze")
    
    else:
        print("Seu ranking é: Barro")
        
num_aleatorio = random.randint(1, 100)
jogo(num_aleatorio)
resp_multiplayer(num_aleatorio)
