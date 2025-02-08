import json

def abrirJSON_Campers():
    dicFinal={}
    with open("./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON_Campers(dic):
    with open("./campers.json",'w') as outFile:
        json.dump(dic,outFile)

def abrirJSON_Trainers():
    dicFinal={}
    with open("./trainers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON_Trainers(dic):
    with open("./trainers.json",'w') as outFile:
        json.dump(dic,outFile)

def agregarEstudiante(estudiantes):
    nuevo_estudiante = {
        "ID": input("Ingrese el ID del estudiante: "),
        "Nombres": input("Ingrese los nombres del estudiante: "),
        "Apellidos": input("Ingrese los apellidos del estudiante: "),
        "Direccion": input("Ingrese la dirección del estudiante: "),
        "Acudiente": input("Ingrese el nombre del acudiente: "),
        "Telefono": input("Ingrese el teléfono del estudiante: "),
        "Estado": input("Ingrese el estado del estudiante: "),
        "Ruta": input("Ingrese la ruta del estudiante: "),
        "Salon": input("Ingrese el salón del estudiante: ")
    }
    estudiantes["estudiantes"].append(nuevo_estudiante)
    guardarJSON_Campers(estudiantes)
    print("Estudiante agregado exitosamente.")

def quitarEstudiante(estudiantes):
    id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")
    for estudiante in estudiantes["estudiantes"]:
        if estudiante["ID"] == id_estudiante:
            estudiantes["estudiantes"].remove(estudiante)
            guardarJSON_Campers(estudiantes)
            print("Estudiante eliminado exitosamente.")
            return
    print("Estudiante no encontrado.")

############################################################################################################################################################
print("\nBienvenido a campuslands, ¿Que eres?")
print("1. Camper")
print("2. Trainer")
print("3. Coordinador")
usuario=int(input("Ingrese el número de la opción: "))
inicio=True
while inicio:
    if usuario==1:
        print("\nBienvenido Camper")
        print("¿Qué desea hacer?")
        print("1. Ver notas")
        print("2. Ver estado")
        print("3. Ver salon")
        opcion=int(input("Ingrese el número de la opción: "))
        if opcion==1:
            print("cursos")

    elif usuario==2:
        print("\nBienvenido Trainer")
        print("¿Qué desea hacer?")
        print("1. Ver campers")
        opcion=int(input("Ingrese el número de la opción: "))
        if opcion==1:
            Estudiantes={}
            Estudiantes=abrirJSON_Campers()
            for i in range(len(Estudiantes["estudiantes"])):
                print("\nEstudiantes:",i+1)
                print("ID:",Estudiantes["estudiantes"][i]["ID"])
                print("Nombre:",Estudiantes["estudiantes"][i]["Nombres"])
                print("Apellido:",Estudiantes["estudiantes"][i]["Apellidos"])
                print("Direccion:",Estudiantes["estudiantes"][i]["Direccion"])
                print("Acudiente:",Estudiantes["estudiantes"][i]["Acudiente"])
                print("Telefono:",Estudiantes["estudiantes"][i]["Telefono"])
                print("Estado:",Estudiantes["estudiantes"][i]["Estado"])
                print("Ruta:",Estudiantes["estudiantes"][i]["Ruta"])
                print("Salon:",Estudiantes["estudiantes"][i]["Salon"])

    elif usuario==3:
        print("\nBienvenido Coordinador")
        print("1. Ver campers")
        print("2. Ver trainers")
        print("3. Agregar estudiante")
        print("4. Quitar estudiante")
        opcion=int(input("¿Qué desea hacer?"))
        Estudiantes={}
        Estudiantes=abrirJSON_Campers()
        if opcion==1:
            for i in range(len(Estudiantes["estudiantes"])):
                print("\nEstudiantes:",i+1)
                print("ID:",Estudiantes["estudiantes"][i]["ID"])
                print("Nombre:",Estudiantes["estudiantes"][i]["Nombres"])
                print("Apellido:",Estudiantes["estudiantes"][i]["Apellidos"])
                print("Direccion:",Estudiantes["estudiantes"][i]["Direccion"])
                print("Acudiente:",Estudiantes["estudiantes"][i]["Acudiente"])
                print("Telefono:",Estudiantes["estudiantes"][i]["Telefono"])
                print("Estado:",Estudiantes["estudiantes"][i]["Estado"])
                print("Ruta:",Estudiantes["estudiantes"][i]["Ruta"])
                print("Salon:",Estudiantes["estudiantes"][i]["Salon"])
        elif opcion==2:
            Trainers={}
            Trainers=abrirJSON_Trainers()
            for i in range(len(Trainers["trainers"])):
                print("\nTrainers:",i+1)
                print("ID:",Trainers["trainers"][i]["ID"])
                print("Nombre:",Trainers["trainers"][i]["Nombres"])
                print("Apellido:",Trainers["trainers"][i]["Apellidos"])
                print("Direccion:",Trainers["trainers"][i]["Direccion"])
                print("Telefono:",Trainers["trainers"][i]["Telefono"])
        elif opcion==3:
            agregarEstudiante(Estudiantes)
        elif opcion==4:
            quitarEstudiante(Estudiantes)
        else:
            print("Opción inválida")

    else:
        inicio=False
        print("Opción inválida")