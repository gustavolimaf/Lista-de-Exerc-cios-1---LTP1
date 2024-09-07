import random

empates = 0
vitoriasUsuario = 0
vitoriasMaquina = 0

opcoes = ['pedra', 'papel', 'tesoura']

while True:
    jogadaUsuario = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
    if jogadaUsuario == 'sair':
        break
    if jogadaUsuario not in opcoes:
        print("Escolha inválida! Releia as opções!")
        continue

    jogadaMaquina = random.choice(opcoes)
    print(f"A máquina escolheu: {jogadaMaquina}")

    if jogadaUsuario == jogadaMaquina:
        print("Empate!")
        empates += 1
    elif (jogadaUsuario == 'pedra' and jogadaMaquina == 'tesoura') or \
            (jogadaUsuario == 'papel' and jogadaMaquina == 'pedra') or \
            (jogadaUsuario == 'tesoura' and jogadaMaquina == 'papel'):
        print("Você venceu!")
        vitoriasUsuario += 1
    else:
        print("A máquina venceu!")
        vitoriasMaquina += 1

if vitoriasMaquina > vitoriasUsuario:
    resultado = 'A máquina venceu no geral!'
elif vitoriasMaquina < vitoriasUsuario:
    resultado = 'Você venceu no geral!'
else:
    resultado = 'Empate geral'

print(f"\nResultado final: {resultado}"
      f"\nVitórias do usuário: {vitoriasUsuario}"
      f"\nVitórias da máquina: {vitoriasMaquina}"
      f"\nEmpates: {empates}")