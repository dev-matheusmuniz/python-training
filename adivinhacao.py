import random

def iniciar_adivinhacao():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print("Níveis de dificuldade:")
    print("(1) Fácil | (2) Médio | (3) Difícil")

    nivel = int(input("Insira a dificuldade desejada: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        if(chute < 1 or chute > 100):
            print("Seu número está fora do range solicitado!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou! Sua pontuação final foi: {}".format(pontos))
            break
        else:
            if(maior):
                print("Seu chute foi maior do que o número secreto!")
            elif(menor):
                print("Seu chute foi menor que o número secreto!")
            
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    iniciar_adivinhacao()