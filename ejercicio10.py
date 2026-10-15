suma = 0
contador = 0

nota = float(input('Ingrese una nota (-1 para terminar): '))

while nota != -1:
    suma = suma + nota
    contador = contador + 1

    nota = float(input('Ingrese otra nota (-1 para terminar): '))

if contador > 0:
    promedio = suma / contador
    print(f'El promedio exacto es de: {promedio}')
else:
    print('No se ingresaron notas')