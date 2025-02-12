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

def NuevoSalon(nombre, horario, ruta):
    return {
        "Nombre": nombre,
        "Horario": horario,
        "Ruta": ruta,
        "Grupo": [],
        "Trainer": {},
        "Skills": []
    }

def EliminarSalon(salones, nombre):
    for salon in salones["Salones"]:
        if salon["Nombre"] == nombre:
            salones["Salones"].remove(salon)
            guardarJSON_salones(salones)
            print("Salón eliminado exitosamente.")
            return
    print("Salón no encontrado.")

def asignarCampersASalon(estudiantes, salones):
    for estudiante in estudiantes["estudiantes"]:
        for salon in salones["Salones"]:
            if estudiante["Disponibilidad"] == salon["Horario"] and estudiante["Ruta"] == salon["Ruta"]:
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