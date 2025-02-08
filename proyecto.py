import json

def abrirJSON():
    dicFinal={}
    with open("./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./campers.json",'w') as outFile:
        json.dump(dic,outFile)
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
            Estudiantes=abrirJSON()
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
        print("Bienvenido Coordinador")
        print("1. Ver campers")
        print("2. Ver trainers")
        print
        opcion=int(input("¿Qué desea hacer?"))
        if opcion==1:
            Estudiantes={}
            Estudiantes=abrirJSON()
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

    else:
        inicio=False
        print("Opción inválida")