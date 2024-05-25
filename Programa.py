Suma = 0
ucs = 0

alumnos = [{"dni": "27502418", "nombre": "Carlos", "apellido": "Mendoza"},
           {"dni": "30550318", "nombre": "Freddy", "apellido": "Mendez"},
           {"dni": "30213555", "nombre": "Laura",  "apellido": "Heredia"}
           ]

fecha_nacimento= [{"dni": "27502418", "día": "07", "mes":"08","año":"1999"},
                  {"dni": "30550318", "día": "15", "mes":"04","año":"2003"},
                  {"dni": "30213555", "día": "28", "mes": "07","año":"2002"}
                  ]

notas = [{"dni": "27502418", "Curso": "MAT31016", "nota": 15},
         {"dni": "30550318", "Curso": "MAT31017", "nota": 16},
         {"dni": "30550318", "Curso": "MAT31016", "nota": 15},
         {"dni": "27502418", "Curso": "MAT31017", "nota": 14},
         {"dni": "30213555", "Curso": "MAT31016", "nota": 16},
         {"dni": "30213555", "Curso": "MAT31017", "nota": 16}]

materia = [{"Curso": "MAT31016", "UC": 3},
           {"Curso": "MAT31017", "UC": 4}]


def fecha_nacimiento (Valor):
    for item in fecha_nacimento:
        if (item ["dni"]==Valor):
            return item ["fecha_nacimiento"]

def nombre_del_alumno(Valor):
    for item in alumnos:
        if (item["dni"] == Valor):
            return item["nombre"]

def apellido(Valor):
    for item in alumnos:
        if(item["dni"]==Valor):
            return item ["apellido"]  

def nombre_y_apellido(Valor):
    for item in alumnos:
        buscar= input ("ingresar cedula: ")
        if(item["dni"]==Valor):
            return item ["nombre"]+" "+ item["apellido"]

def agregar_alumno():
    nuevo_dni = input("Ingrese el DNI del nuevo estudiante: ")
    if nuevo_dni in [alumno["dni"] for alumno in alumnos]:
        print(f"Error: El estudiante con DNI '{nuevo_dni}' ya existe.")
        return

    nuevo_nombre = input("Ingrese el nombre del nuevo estudiante: ")
    nuevo_apellido = input("Ingrese el apellido del nuevo estudiante: ")

    # Agregar la información del nuevo estudiante a las listas correspondientes
    alumnos.append({"dni": nuevo_dni, "nombre": nuevo_nombre, "apellido": nuevo_apellido})
    fecha_nacimento.append({"dni": nuevo_dni, "día": input("Ingrese el día de nacimiento: "),
                             "mes": input("Ingrese el mes de nacimiento: "),
                             "año": input("Ingrese el año de nacimiento: ")})
    notas.append({"dni": nuevo_dni, "Curso": input("Ingrese el código del curso: "), "nota": float(input("Ingrese la nota: "))})

    print(f"Estudiante '{nuevo_nombre} {nuevo_apellido}' agregado correctamente.")

def calculo(item): #operacion que calcula el promedio ponderado
    for row in materia:
        global Suma
        global ucs
        if (row["Curso"] == item["Curso"]):
            Suma += item["nota"] * row["UC"]
            ucs += row["UC"]

def buscar (): #para introducir la cedula
    buscar= input ("ingresar cedula: ")

def salida ():
    confirmacion = input("¿Desea realizar otra operación? (s/n): ")
    if confirmacion.lower() == 'n':
        print("Saliendo del programa...")
        exit()
    else:
            mostrar_menu()
            opcion = input("Ingrese la opción deseada: ")
            menu_opcion(opcion)

def mostrar_menu():
     print("\n" .join([
         ""
         "1. Nombre",
         "2. Apellido",
         "3. Nombre completo",
         "4. Fecha de Nacimento",
         "5. Promedio Ponderado",
         "6" "Agregar alumno",
         "7. Salir"
     ]))

def menu_opcion(opcion):
    if opcion == '1': #arroja nombre
        buscar ()
        vnombre = nombre_del_alumno (buscar)
        print(f"El nombre del alumno es: {vnombre}")
        salida()
        
        
    elif opcion == '2': #arroja apellido
        buscar()
        vapellido= apellido(buscar)
        print(f"El apellido del alumno es: {vapellido}")
        salida ()

    elif opcion == '3': #nombre+apellido
        buscar()
        for item in alumnos:
            if item["dni"] == buscar:
                nombre_y_apellido (item)
        print(item ["nombre"]+" "+ item["apellido"])
        salida()

    elif opcion == '4': #fecha de nacimiento
        buscar()
        for Valor in fecha_nacimento:
            if Valor["dni"] == buscar:
                fecha_nacimiento(Valor)
        print(Valor["día"]+"/"+Valor["mes"]+"/"+Valor["año"])
        salida()

    elif opcion == '5': #promedio
        buscar()
        for item in notas:
            if item["dni"] == buscar:
                calculo(item)
        prom = Suma / ucs
        print(f"El promedio ponderado es de: {prom:.2f}")
        salida()

    elif opcion == '6': #salida
        agregar_alumno()
        salida()
    elif opcion == '7':
        salida()
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        salida()
        
mostrar_menu()
opcion = input("Ingrese la opción deseada: ")
menu_opcion(opcion)