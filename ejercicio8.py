print('Suma Indefinida de Números')

suma = 0

while True:
    num = int(input('Ingrese un número (0 para terminar): '))
    suma += num
    
    if num == 0:
        break
    
print(f'La suma de los números ingresados es: {suma}')