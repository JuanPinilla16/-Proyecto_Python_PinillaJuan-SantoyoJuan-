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

def abrirJSON_salones():
    dicFinal={}
    with open("./salones.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON_salones(dic):
    with open("./salones.json",'w') as outFile:
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
        "Ruta": "Sin asignar",
        "Grupo": input("Ingrese el grupo del estudiante(A,B,C)"),
        "Notas": "Sin asignar",
        "Disponibilidad": input("Ingrese la disponibilidad del estudiante (Mañana, Tarde): ")}
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
        "Ruta": input("Ingrese la ruta del trainer (Java, NodeJs, NetCore): ")
    }
    trainers["trainers"].append(nuevo_trainer)
    guardarJSON_Trainers(trainers)
    print("Trainer agregado exitosamente.")

def quitarTrainer(trainers):
    id_trainer = input("Ingrese el ID del trainer a eliminar: ")
    for trainer in trainers["trainers"]:
        if trainer["ID"] == id_trainer:
            trainers["trainers"].remove(trainer)
            guardarJSON_Trainers(trainers)
            print("Trainer eliminado exitosamente.")
            return
    print("Trainer no encontrado.")

def asignarCampersASalon(estudiantes, salones):
    for estudiante in estudiantes["estudiantes"]:
        for salon in salones["Salones"]:
            if estudiante["Disponibilidad"] == salon["Horario"]:
                salon["Grupo"].append({
                    "ID": estudiante["ID"],
                    "Nombre": estudiante["Nombres"],
                    "Apellido": estudiante["Apellidos"],
                    "Ruta": estudiante["Ruta"]
                })
                break
    guardarJSON_salones(salones)
    print("Estudiantes asignados a los salones exitosamente.")

def asignarTrainerASalon(trainers, salones):
    for trainer in trainers["trainers"]:
        for salon in salones["Salones"]:
            if trainer["Ruta"] == salon["Ruta"]:
                salon["Trainer"] = {
                    "ID": trainer["ID"],
                    "Nombre": trainer["Nombres"],
                    "Apellido": trainer["Apellidos"],
                    "Ruta": trainer["Ruta"]
                }
                break
    guardarJSON_salones(salones)
    print("Trainer asignado a los salones exitosamente.")

def vaciarSalones(salones):
    for salon in salones["Salones"]:
        salon["Grupo"] = []
        salon["Trainer"] = {}
    guardarJSON_salones(salones)
    print("Salones vaciados exitosamente.")

def verSalones(salones):
    for salon in salones["Salones"]:
        print("\nSalon:", salon["Nombre"])
        print("Horario:", salon["Horario"])
        print("Ruta:", salon["Ruta"])
        print("Estudiantes:")
        for estudiante in salon["Grupo"]:
            print("  ID:", estudiante["ID"])
            print("  Nombre:", estudiante["Nombre"])
            print("  Apellido:", estudiante["Apellido"])
        print("------------------------------------------------------")
def CampersInscritos(estudiantes):
    for i in range(len(estudiantes["estudiantes"])):
        if estudiantes["estudiantes"][i]["Estado"]=="Inscrito":
            print("Nombre:",estudiantes["estudiantes"][i]["Nombres"],estudiantes["estudiantes"][i]["Apellidos"])
            print("ID:",estudiantes["estudiantes"][i]["ID"])
            print("Ruta:",estudiantes["estudiantes"][i]["Ruta"])
            print("Grupo:",estudiantes["estudiantes"][i]["Grupo"])
            print("Disponibilidad:",estudiantes["estudiantes"][i]["Disponibilidad"])
            print("Estado:",estudiantes["estudiantes"][i]["Estado"])
            
            print("\n")

def CampersAprobados(estudiantes):
    for i in range(len(estudiantes["estudiantes"])):
        if estudiantes["estudiantes"][i]["Estado"]=="Aprobado":
            print("Nombre:",estudiantes["estudiantes"][i]["Nombres"],estudiantes["estudiantes"][i]["Apellidos"])
            print("ID:",estudiantes["estudiantes"][i]["ID"])
            print("Ruta:",estudiantes["estudiantes"][i]["Ruta"])
            print("Grupo:",estudiantes["estudiantes"][i]["Grupo"])
            print("Disponibilidad:",estudiantes["estudiantes"][i]["Disponibilidad"])
            print("Estado:",estudiantes["estudiantes"][i]["Estado"])
            
            print("\n")
def NotasDelCamper(teorica,practica,trabajos):
    porcentaje_teorica=teorica*0.30
    porcentaje_practica=practica*0.60
    porcentaje_trabajos=trabajos*0.10
    notaFinal=porcentaje_teorica+porcentaje_practica+porcentaje_trabajos
    return notaFinal

############################################################################################################################################################
InicioDeTodo=True
while InicioDeTodo:
    print("\nBienvenido a campuslands, ¿Que eres?")
    print("1. Camper")
    print("2. Trainer")
    print("3. Coordinador")
    usuario=int(input("Ingrese el número de la opción: "))
    inicio=True
    while inicio:
        if usuario==1:
            Estudiantes={}
            Estudiantes=abrirJSON_Campers()
            print("Ingrese su ID")
            ID=input("ID: ")
            for estudiante in Estudiantes["estudiantes"]:
                if estudiante["ID"]==ID:
                    inicioCamp=True
                    print("Hola",estudiante["Nombres"],estudiante["Apellidos"])
                    print("\n")
                    while inicioCamp:
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
                        print("4. Salir")
                        print("------------------------------------------------------")
                        opcion=int(input("Ingrese el número de la opción: "))
                        if opcion==1:
                            print("notas: ",estudiante["Notas"])
                        if opcion==2:
                            for i in range(len(Estudiantes["estudiantes"])):
                                idd=Estudiantes["estudiantes"][i]["ID"]
                                if idd==ID:
                                    estado=Estudiantes["estudiantes"][i]["Estado"]
                                    print("Estado:",estado)
                        if opcion==3:
                            Salones={}
                            Salones=abrirJSON_salones()
                            for salon in Salones["Salones"]:
                                for estudiante in salon["Grupo"]:
                                    if estudiante["ID"]==ID:
                                        print("Salon:",salon["Nombre"])
                                        print("Horario:",salon["Horario"])
                                        print("Ruta:",salon["Ruta"])
                        if opcion==4:
                            inicio=False
                            inicioCamp=False
                            print("Hasta luego")
    ############################################################################################################################################################

        elif usuario==2:
            Trainers={}
            Trainers=abrirJSON_Trainers()
            print("Ingrese su ID")
            ID=input("ID: ")
            for trainer in Trainers["trainers"]:
                if trainer["ID"]==ID:
                    inicioTrainer=True
                    print("Hola",trainer["Nombres"],trainer["Apellidos"])
                    print("\n")
                    while inicioTrainer:
                        print("            Bienvenido Trainer                        ")
                        print("¿Qué desea hacer?")
                        print("------------------------------------------------------")
                        print("1. Ver campers")
                        print("------------------------------------------------------")
                        print("2. Ver salones")
                        print("------------------------------------------------------")
                        print("3. Asignar notas")
                        print("------------------------------------------------------")
                        print("4. Salir")
                        print("------------------------------------------------------")
                        opcion=int(input("Ingrese el número de la opción: "))
                        Estudiantes={}
                        Estudiantes=abrirJSON_Campers()
                        Salones={}
                        Salones=abrirJSON_salones()
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
                                print("Grupo:",Estudiantes["estudiantes"][i]["Grupo"])
                                print("Notas:",Estudiantes["estudiantes"][i]["Notas"])
                                print("Disponibilidad:",Estudiantes["estudiantes"][i]["Disponibilidad"])
                        elif opcion==2:
                            verSalones(Salones)
                        elif opcion==3:
                            print("Ingrese el ID del camper")
                            ID=input("ID: ")
                            for estudiante in Estudiantes["estudiantes"]:
                                if estudiante["ID"]==ID:
                                    print("Ingrese la nota de la prueba teórica")
                                    teorica=float(input("Nota: "))
                                    print("Ingrese la nota de la prueba práctica")
                                    practica=float(input("Nota: "))
                                    print("Ingrese la nota de los trabajos")
                                    trabajos=float(input("Nota: "))
                                    notaFinal=NotasDelCamper(teorica,practica,trabajos)
                                    if notaFinal>=60:
                                        estudiante["Notas"]="Si pasaron"
                                    else:
                                        estudiante["Notas"]="Rendimiento Bajo"
                                        print("Nota final:",notaFinal)
                                    guardarJSON_Campers(Estudiantes)
                                
                        elif opcion==4:
                            inicio=False
                            inicioTrainer=False
                            print("Hasta luego")
    ############################################################################################################################################################
        elif usuario==3:
            print("\n")
            print("                Bienvenido Coordinador                ")
            print("------------------------------------------------------")
            print("1. Ver campers")
            print("------------------------------------------------------")
            print("2. Ver trainers")
            print("------------------------------------------------------")
            print("3. Ver salones")
            print("------------------------------------------------------")
            print("4. Agregar estudiante")
            print("------------------------------------------------------")
            print("5. Quitar estudiante")
            print("------------------------------------------------------")
            print("6. Agregar trainer")
            print("------------------------------------------------------")
            print("7. Quitar trainer")
            print("------------------------------------------------------")
            print("8. Asignar campers a salon")
            print("------------------------------------------------------")
            print("9. Asignar trainer a salon")
            print("------------------------------------------------------")
            print("10. Vaciar salones")
            print("------------------------------------------------------")
            print("11. Campers Inscritos")
            print("------------------------------------------------------")
            print("12. Campers Aprobados")
            print("------------------------------------------------------")
            print("13. Campers En rendimiento bajo")
            print("------------------------------------------------------")
            print("14. Campers que pasaron y Campers que perdieron ")
            print("------------------------------------------------------")
            print("15. Salir")
            print("------------------------------------------------------")
            opcion=int(input("\n¿Qué desea hacer?: "))
            Estudiantes={}
            Estudiantes=abrirJSON_Campers()
            Trainers={}
            Trainers=abrirJSON_Trainers()
            Salones={}
            Salones=abrirJSON_salones()
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
                    print("Grupo:",Estudiantes["estudiantes"][i]["Grupo"])
                    print("Notas:",Estudiantes["estudiantes"][i]["Notas"])
                    print("Disponibilidad:",Estudiantes["estudiantes"][i]["Disponibilidad"])
            elif opcion==2:
                for i in range(len(Trainers["trainers"])):
                    print("\nTrainers:",i+1)
                    print("ID:",Trainers["trainers"][i]["ID"])
                    print("Nombre:",Trainers["trainers"][i]["Nombres"])
                    print("Apellido:",Trainers["trainers"][i]["Apellidos"])
                    print("Ruta:",Trainers["trainers"][i]["Ruta"])
            elif opcion==3:
                verSalones(Salones)
            elif opcion==4:
                agregarEstudiante(Estudiantes)
            elif opcion==5:
                quitarEstudiante(Estudiantes)
            elif opcion==6:
                agregarTrainer(Trainers)
            elif opcion==7:
                quitarTrainer(Trainers)
            elif opcion==8:
                asignarCampersASalon(Estudiantes, Salones)
            elif opcion==9:
                asignarTrainerASalon(Trainers, Salones)
            elif opcion==10:
                vaciarSalones(Salones)
            elif opcion==11:
                CampersInscritos(Estudiantes)
            elif opcion==12:
                CampersAprobados(Estudiantes)
            elif opcion==13:
                for i in range(len(Estudiantes["estudiantes"])):
                    if Estudiantes["estudiantes"][i]["Notas"]=="Rendimiento Bajo":
                        print("Nombre:",Estudiantes["estudiantes"][i]["Nombres"],Estudiantes["estudiantes"][i]["Apellidos"])
                        print("ID:",Estudiantes["estudiantes"][i]["ID"])
                        print("Ruta:",Estudiantes["estudiantes"][i]["Ruta"])
                        print("Grupo:",Estudiantes["estudiantes"][i]["Grupo"])
                        print("Disponibilidad:",Estudiantes["estudiantes"][i]["Disponibilidad"])
                        print("Estado:",Estudiantes["estudiantes"][i]["Estado"])
                        print("Notas:",Estudiantes["estudiantes"][i]["Notas"])
                        print("\n")
            elif opcion==14:
                Sipasaron=0
                rendimientoBajo=0
                for i in range(len(Estudiantes["estudiantes"])):
                    if Estudiantes["estudiantes"][i]["Notas"]=="Si pasaron":
                        Sipasaron+=1
                    elif Estudiantes["estudiantes"][i]["Notas"]=="Rendimiento Bajo":
                        rendimientoBajo+=1
                print("\n")
                print("Campers que pasaron:",Sipasaron)
                print("Campers que perdieron:",rendimientoBajo)
            elif opcion==15:
                inicio=False
                print("Hasta luego")
            else:
                print("Opción inválida")

        else:
            inicio=False
            print("Opción inválida")