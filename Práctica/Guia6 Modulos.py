import Modulos
#Ese Modulo es un archivo que se llama Modulos (está entre todos los archivos también sí)
# b= Modulos.filtrar((1,2,3,4),"par")
# print(b)
# #Why is so boring

# #Ejercicio 2
# texto1= "Me"
# texto2= "Divierto"
# print(Modulos.concatenar(texto1,texto2))
# print(Modulos.reemplazar("Hola soy Alesio, como estan Alesio, Alesio vieron", "Alesio", "Fry"))
# print(Modulos.mayuscular("hola gente"))
# print(Modulos.contarletrar("HOla mundo Como Gente","e"))

#Modulos estandar
import math
#Ejercicio 3
#Grados radianes
# def gradian(n):
#     return n* math.pi /180
# print(gradian(90))

# Confío en que van a saber hacer el Ejercicio 4

#Ejercicio 5
#Perimetro
# def perimetro(radio):
#     return 2* math.pi*radio

#Ejercicio 6
#Adivinar numero random
import random
# numero=random.randint(1,100)
# maxintentos= int(input("Ingrese el número máximo de intentos: "))
# i=1
# while i<=maxintentos:
#     b=int(input("Ingrese su número: "))
#     if numero>b:
#         print("Su número elegido es menor que el random")
#     if numero<b:
#         print("Su número elegido es mayor que el número random")
#     if numero==b:
#         print("Felicitaciones, ganaste")
#         break
#     print(i)
#     i=i+1
# if b!=numero:
#     print("Alcanzó el número máximo de intentos")

#Ejercicio 7
#Dado
# def dado():
#     return random.randint(1,6)
# print(dado())

#Ejercicio 8
#Elegir nombres
# def elegirnombre(nombres):
#     nombreelegido=random.choice(nombres)
#     return nombreelegido
# nombres=["Alesio","Maddi", "Juan", "nose","Lucia", "Argentina"]
# print(elegirnombre(nombres))

#Ejercicio 9
#Fecha y hora
import datetime
def fechayhora():
    fecha=datetime.datetime.now()
    hora=datetime.datetime.now().time()
    return fecha.date(),hora
# print(fechayhora())

#Ejercicio 10 (este lo hizo chat gpt)
#Fecha de cumpleaños
def distanciatemporal(fechadenacimiento):
    formato_fecha = "%Y-%m-%d"
    
    # Convertir la entrada del usuario en un objeto datetime
    Nacimiento= datetime.datetime.strptime(fechadenacimiento, formato_fecha)
    # Obtener la fecha y hora actuales
    hoy = datetime.datetime.now()
    # Calcular la diferencia entre las fechas
    diferencia = hoy - Nacimiento
    return diferencia.days
# print(distanciatemporal("2003-6-11"))

#Ejercicio 11 
#Edad y peso en otro planeta
def pesoedadplaneta(fehcadenac,peso,):
    import random
    dias=distanciatemporal(fehcadenac)
    planetas=["Mercurio", "Venus", "Marte", "Jupiter"]
    Años={"Mercurio":88, "Venus":225, "Marte":687,"Jupiter": 12*365}
    ges={"Mercurio":0.38, "Venus":0.91, "Marte":0.38,"Jupiter": 2.34}

    planetarandom= random.choice(planetas)
    añosenplaneta= dias//Años[planetarandom]
    pesoenplaneta= peso/9.81 * ges[planetarandom]
    return planetarandom,añosenplaneta,pesoenplaneta
#print(pesoedadplaneta("2003-06-11",85))





