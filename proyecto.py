import json

def abrirJSON():
    dicFinal={}
    with open("./Estudiantes.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Estudiantes.json",'w') as outFile:
        json.dump(dic,outFile)
########################################################################################################################################
print("Bienvenido a campuslands, ¿Que eres? (1. Camper, 2. Trainer, 3. Coordinador): ")
usuario=input("Ingresa: ")
print("\n")

inicio=True
while inicio == True:
    print("Bienvenido a campuslands")
    print("1. Estudiantes")
    opc=int(input("\nIngresa lo que quieres hacer: "))
    if opc == 3:
        print("\n")
        Estudiantes={}
        Estudiantes=abrirJSON()
        for i in range(len(Estudiantes["estudiantes"])):
            print("\n estudiante #: ", i+1)
            print("Numero de ID: ", Estudiantes["estudiantes"][i]["# de identificacion"])
            print("Nombres: ", Estudiantes["estudiantes"][i]["Nombres"])
            print("Apellidos: ", Estudiantes["estudiantes"][i]["Apellidos"])
            print("Direccion: ", Estudiantes["estudiantes"][i]["Direccion"])
            print("Acudiente: ", Estudiantes["estudiantes"][i]["Acudiente"])
            print("Telefono de contacto (celular y fijo): ", Estudiantes["estudiantes"][i]["Telefono de contacto (celular y fijo)"])
    elif opc==5:
        inicio=False
        print("Error")