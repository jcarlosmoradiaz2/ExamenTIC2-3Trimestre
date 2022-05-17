import random


# ----  Ejercicios ---- 

#Ejercicio 1
def menu():
    print("1-Guardar asignatura")
    print("2-Borrar asignatura")
    print("3-Ver nota media")
    print("4-Ver todas las asignaturas")
    print("5-Salir")
    opcion=0
    while(opcion<1 or opcion>5):
        try:
            opcion=(int)(input("Dime la opción que deseas:..."))
        except:
            opcion=0
    return opcion
#Fin ejercicio 1




#Ejercicio 3
def opcion1(asignaturas):
    asignatura1=str(input("Introduzca la asignatura:..."))
    asignaturas.append(asignatura1)
    return asignaturas
#Fin ejercicio 3




#Ejercicio 4
def opcion2(asignaturas):
    nombreasignatura=input("Introduzca el nombre de una asignatura:...")
    try:
        asignaturas.remove(nombreasignatura)
        return True
    except:
        return False
#Fin ejercicio 4



#Ejercicio 5
def funcion5(elementos):
    lista=[]
    for i in range(elementos):
        lista=random.randint(0,10)
    return lista
#Fin ejercicio 5



#Ejercicio6
def medianotas():
    notas=funcion5(5)
    suma=0
    media=0
    for i in notas:
        suma= suma+i
    media= (suma/len(notas))
    return media
    
#Fin ejercicio 6


#Ejercicio7
def ejercicio4(asignaturas):
    print("*** Asignaturas matriculadas ***")
    contador = 0

    for i in asignaturas:
        contador = contador + 1

    for i in range(0, contador):
        print(i+1, "-", asignaturas[i])

    print("*** Fin asignaturas matriculadas ***")




#Fin ejercicio7








# ---- Programa principal -----
#Ejercicio 2
opcion=menu()
asignaturas=[]
while opcion!=5:
    if (opcion==5):
        break
    if opcion==1:
        print(opcion1(asignaturas))
    if opcion==2:
        verdaderofalso=opcion2(asignaturas)
        if verdaderofalso==True:
            print ("Asignatura borrada")
        else:
            print ("No se ha podido borrar")
    if opcion==3:
        medianotas()
    if opcion==4:
        ejercicio4(asignaturas)





    opcion=menu()
    


