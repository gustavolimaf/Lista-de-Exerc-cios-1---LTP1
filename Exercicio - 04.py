notas = [6.3, 7.5, 9.2, 5.1, 6.8]
soma = 0
notasAcimaMedia = 0

for nota in notas:
    soma += nota
    if nota > 6:
        notasAcimaMedia += 1
media = soma / len(notas)

print(f"A média é: {media:.2f}")
print('Notas acima de 6: {}'.format(notasAcimaMedia))