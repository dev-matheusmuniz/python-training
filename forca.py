def iniciar_forca():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper() #using strip to remove all spaces and upper to make it all in capital letters

        if (chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if(chute == letra): 
                    letras_acertadas[i] = letra
                i += 1
        else:
            erros += 1
            print("Você errou, restam apenas {} tentativas.".format(6-erros))
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    iniciar_forca()