print ('Validación de Nota Positiva')

nota = float(input('Ingrese la calificación (0.0 - 5.0): '))

while nota < 0 or nota > 5:
    print('Error, la calificación debe estar entre 0.0 y 5.0')
    nota = float(input('Ingrese la calificación (0.0 - 5.0): '))

print(f'La nota ingresada es: {nota}')