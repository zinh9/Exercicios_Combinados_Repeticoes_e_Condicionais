import random

print("Bem vindos ao jogo de adivinhação!!!\nNesse jogo você deve adivinhar/chutar qual numero o programa escolheu.\nVocê começa com o total de 100 pontos, a cada vez que você erra um numero você perde 10 pontos, e a cada dica vpcê perde 5 pontos.\n")

print("Ranking:\nDiamante: 100 pontos\nOuro: 75 pontos\nPrata: 50 pontos\nBronze: 25 pontos\nBarro: 0 pontos\n")

def adivinha(num_aleatorio):
    chute = []
    pontos = 100
    i = 0
    
    while i < 10:
        chute.append(int(input("Qual numero o programa escolheu: ")))
        
        if chute[i] != num_aleatorio:
            pontos -= 10
            
        elif chute[i] == num_aleatorio:
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
                dicas(i)
                pontos -= 5
        
        i += 1

def dicas(i):
    dica = random.randint(1, 4)
                
    if dica == 1 and num_aleatorio % 2 == 0:
        print("O numero é par")
                
    elif dica == 2 and num_aleatorio % 2 == 1:
        print("O numero é impar")
                
    elif dica == 3 and num_aleatorio > 50:
        print("O numeros é maior que 50")
                
    elif dica == 4 and num_aleatorio < 50:
        print("O numeros é menor que 50")

def ranking(pontos):
    if pontos == 100:
        print("Seu ranking é: Diamante")
    
    elif pontos == 75:
        print("Seu ranking é: Ouro")
    
    elif pontos == 50:
        print("Seu ranking é: Prata")
    
    elif pontos == 25:
        print("Seu ranking é: Bronze")
    
    else:
        print("Seu ranking é: Barro")
        
num_aleatorio = random.randint(1, 100)
adivinha(num_aleatorio)
