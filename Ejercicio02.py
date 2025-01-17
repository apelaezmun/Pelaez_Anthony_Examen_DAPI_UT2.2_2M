alumnos = {}
opciones = ''
n = 0
while opciones != '4':
    if opciones == '1':
        nombre = input('Nombre del alumno: ')
        nota = (input('El alumno esta aprobado o suspendido: '))
        alumnos['nombre'] = nombre
        alumnos['nota'] = nota
        if nota == 'aprobado':
             nota = True
        else:
             nota = False
    elif opciones == '2':
        if nota in alumnos == True:
             n = n + 1
             print('El numero de alumnos aprobados son:', n)
        else:
            print('El numero de alumnos aprobados son:', 0)
    elif opciones == '3':
            print(alumnos)
    opciones = input('Opciones\n(1) Añadir alumno\n(2) Numero de aprobados\n'
                     '(3) Mostrar todo el alumnado\n(4) Terminar\nElige una '
                     'opcion: ')