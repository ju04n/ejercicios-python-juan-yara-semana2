base = int(input('Ingrese la base: '))

exponente = int(input('Ingrese el exponente: '))

resultado = 1
contador = 0

while contador < exponente:
    resultado = resultado * base
    contador = contador + 1

print(f'El resultado es: {resultado}')