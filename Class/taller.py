try:
    registro = int (input('Cuantas personas desea registrar? '))

    for  i in range(registro):
        print('registros de pariticipantes', i+1)
        nombres = input ('ingrese sus nombres: ')
   
        edad = float(input('ingrese su edad: '))
        h = input ('Tiene conocimientos previos? (si/no) ')

        if (edad >14 and h.lower() == 'si'):
            print ('Puede asistir')

        elif (edad < 0):
            print ('Error, coloque edad positiva')

        else: 
            print('No cumple los requsitos')

except ValueError:
    print ('No ingrese letra donde van los numeros.')

print ('Proceso finalizado')