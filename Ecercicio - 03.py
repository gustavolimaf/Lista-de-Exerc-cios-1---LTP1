n = 10

fibonacci = [0, 1]

for i in range(2, n):
    proximo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)
print('Os 10 primeiros números da sequênncia de Fibonacci são: ',fibonacci)