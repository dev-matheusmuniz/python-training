def iniciar_forca():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip() #using strip to remove all spaces

        i = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #using upper to make it all in capital letters
                letras_acertadas[i] = letra
            i = i+1

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    iniciar_forca()