import random
import os

print("=" * 40)
print("Bem Vindo ao Jogo Pedra, Papel e Tesoura")
print("=" * 40)

placar_vc = 0
placar_comp = 0

while True:
    def resultado(usua, comp):
        if usua == comp:
            return "Empate"
        elif (usua == 1 and comp == 3) or \
                (usua == 2 and comp == 1) or \
                (usua == 3 and comp == 2):
            return "Voce venceu!"
        else:
            return "O computador venceu!"


    escolha = int(input("Digite: 0 - para jogar | 1 - para sair "))
    os.system("cls")

    if escolha == 0:
        numeros = [1, 2, 3]
        usua = int(input("Escolha 1 - para Pedra | 2 - para Papel | 3 - para Tesoura: "))
        if usua == 1:
            print("Você escolheu Pedra!")
        elif usua == 2:
            print("Você escolheu Papel!")
        elif usua == 3:
            print("Você escolheu Tesoura!")
        else:
            print("Escolha Inválida")
            continue

        comp = random.choice(numeros)
        if comp == 1:
            print("O computador escolheu Pedra!")
        elif comp == 2:
            print("O computador escolheu Papel!")
        elif comp == 3:
            print("O computador escolheu Tesoura!")

        resultado_jogo = resultado(usua, comp)
        print(resultado_jogo)

        if resultado_jogo == "Voce venceu!":
            placar_vc += 1
        elif resultado_jogo == "O computador venceu!":
            placar_comp += 1

        print("Placar: Você", placar_vc, "x", placar_comp, "Computador")

    elif escolha == 1:
        break
    else:
        print("Escolha Inválida")
        continue
