print('Selección de Tipo de Documento')

tipo_doc = ['CC', 'TI', 'CE']

doc = ''

while doc not in tipo_doc:
    doc = input('Ingrese su tipo de documento (CC, TI o CE): ').upper()

    if doc not in tipo_doc:
        print('Tipo de documento inválido, intente de nuevo...')

print('Continuando...')