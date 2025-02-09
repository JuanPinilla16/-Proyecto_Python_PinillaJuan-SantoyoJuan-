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
    nuevo_camper = {
        "ID": input("Ingrese el ID del estudiante: "),
        "Nombres": input("Ingrese los nombres del estudiante: "),
        "Apellidos": input("Ingrese los apellidos del estudiante: "),
        "Direccion": input("Ingrese la dirección del estudiante: "),
        "Acudiente": input("Ingrese el nombre del acudiente: "),
        "Telefono": input("Ingrese el teléfono del estudiante: "),
        "Estado": input("Ingrese el estado del estudiante ((En proceso de ingreso, Inscrito, Aprobado,Cursando, Graduado, Expulsado, Retirado): "),
        "Ruta": input("Ingrese la ruta del estudiante: "),
        "Salon": input("Ingrese el salón del estudiante (Artemis, Sputnik, Apollo): ")
    }
    estudiantes["estudiantes"].append(nuevo_camper)
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

def agregarTrainer(trainers):
    nuevo_trainer = {
        "ID": input("Ingrese el ID del trainer: "),
        "Nombres": input("Ingrese los nombres del trainer: "),
        "Apellidos": input("Ingrese los apellidos del trainer: "),
        "Ruta": input("Ingrese la ruta del trainer: ")
    }
    trainers["trainers"].append(nuevo_trainer)
    guardarJSON_Trainers(trainers)
    print("trainer agregado exitosamente.")

def quitarTrainer(trainers):
    id_trainer = input("Ingrese el ID del trainer a eliminar: ")
    for trainer in trainers["trainers"]:
        if trainer["ID"] == id_trainer:
            trainers["trainers"].remove(trainer)
            guardarJSON_Trainers(trainers)
            print("Trainer eliminado exitosamente.")
            return
    print("Trainer no encontrado.")

############################################################################################################################################################
print("\nBienvenido a campuslands, ¿Que eres?")
print("1. Camper")
print("2. Trainer")
print("3. Coordinador")
usuario=int(input("Ingrese el número de la opción: "))
inicio=True
while inicio:
    if usuario==1:
        print("\n")
        print("                 Bienvenido Camper                    ")
        print("¿Qué desea hacer?")
        print("------------------------------------------------------")
        print("1. Ver notas")
        print("------------------------------------------------------")
        print("2. Ver estado")
        print("------------------------------------------------------")
        print("3. Ver salon")
        print("------------------------------------------------------")
        opcion=int(input("Ingrese el número de la opción: "))
        if opcion==1:
            print("cursos")
############################################################################################################################################################

    elif usuario==2:
        print("            Bienvenido Trainer                        ")
        print("¿Qué desea hacer?")
        print("------------------------------------------------------")
        print("1. Ver campers")
        print("------------------------------------------------------")
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
############################################################################################################################################################
    elif usuario==3:
        print("\n")
        print("                Bienvenido Coordinador                ")
        print("------------------------------------------------------")
        print("1. Ver campers")
        print("------------------------------------------------------")
        print("2. Ver trainers")
        print("------------------------------------------------------")
        print("3. Agregar estudiante")
        print("------------------------------------------------------")
        print("4. Quitar estudiante")
        print("------------------------------------------------------")
        print("5. Agregar trainer")
        print("------------------------------------------------------")
        print("6. Quitar trainer")
        print("------------------------------------------------------")
        print("7. volver al menú principal")
        print("------------------------------------------------------")
        opcion=int(input("¿Qué desea hacer?: "))
        Estudiantes={}
        Estudiantes=abrirJSON_Campers()
        Trainers={}
        Trainers=abrirJSON_Trainers()
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
            for i in range(len(Trainers["trainers"])):
                print("\nTrainers:",i+1)
                print("ID:",Trainers["trainers"][i]["ID"])
                print("Nombre:",Trainers["trainers"][i]["Nombres"])
                print("Apellido:",Trainers["trainers"][i]["Apellidos"])
                print("Ruta:",Trainers["trainers"][i]["Ruta"])
        elif opcion==3:
            agregarEstudiante(Estudiantes)
        elif opcion==4:
            quitarEstudiante(Estudiantes)
        elif opcion==5:
            agregarTrainer(Trainers)
        elif opcion==6:
            quitarTrainer(Trainers)
        elif opcion==7:
            inicio=False
        else:
            print("Opción inválida")

    else:
        inicio=False
        print("Opción inválida")