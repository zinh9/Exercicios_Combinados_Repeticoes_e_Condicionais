import random

def adivinha(num_aleatorio):
    chute = []
    i = 0
    
    while chute != num_aleatorio:
        chute.append(int(input("Qual numero o programa escolheu: ")))
        
        if chute[i] == num_aleatorio:
            print("PARABÉNS!!! VOCÊ GANHOU O JOGO COM: ", len(chute),"CHUTES")
            break
        
        elif chute[i] > num_aleatorio:
            print("Um pouco menos")
        
        elif chute[i] < num_aleatorio:
            print("Um pouco mais")
        
        i += 1

num_aleatorio = random.randint(1, 100)
adivinha(num_aleatorio)
