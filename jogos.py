import forca
import adivinhacao

def escolhe_jogo():

        print("*********************************")
        print("*******Escolha o seu jogo!*******")
        print("*********************************")

        print("(1) Forca | (2) Adivinhação")

        jogo = int(input("Escolha o jogo desejado: "))

        if(jogo == 1):
            print("Iniciando Forca...")
            forca.iniciar_forca()
        elif(jogo == 2):
            print("Iniciando Adivinhação...")
            adivinhacao.iniciar_adivinhacao()

if(__name__ == "__main___"):
    escolhe_jogo()