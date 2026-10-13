print ('Intentos Limitados de Inicio de Sesión')

contrasena = int(input('Registre una contraseña (SOLO NÚMEROS): '))

validacion = 0
intentos = 0

while intentos < 3:
    validacion = int(input('Ingrese su contraseña registrada: '))
    intentos += 1

    if validacion == contrasena:
        print('Acceso concedido')
        break
    else:
        print('Error, contraseña incorrecta')
        
if validacion != contrasena:
    print('Cuenta bloqueada')