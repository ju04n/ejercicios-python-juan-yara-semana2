print('Menú Principal de un Sistema')

opcion = 0

while opcion != 3:
    print('\n1. Consultar 2. Registrar 3. Salir')
    
    opcion = int(input('\nIngrese una acción a realizar: '))
    
    if opcion == 1:
        print('Consultando...')
        
    elif opcion == 2:
        print('Registrando...')
        
    elif opcion == 3:
        print('Saliendo...')
        
    else:
        print('Opción inválida, intente de nuevo\n')