print('Factorial de un Número')

num_fact = int(input('Introduce un número para el factorial: '))

factorial = 1

for i in range(1, num_fact + 1):
    factorial *= i

print(f'El factorial de {num_fact} es: {factorial}')