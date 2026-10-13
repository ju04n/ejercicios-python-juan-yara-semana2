print ('Validación de Clave Fija')

contrasena = int(input('Registre una contraseña (SOLO NÚMEROS): '))

validacion = int(input('Ingrese su contraseña registrada: '))


while validacion != contrasena:
    print('Error, contraseña incorrecta')
    validacion = int(input('Ingrese la contraseña de nuevo: '))

print('Acceso concedido')