#Archivos
def escrenglones(archivo,renglon):
    with open(archivo,"w") as algo:
        for i in renglon:
            algo.write(str(i)+"\n")

def imprimir(nombre):
    with open(nombre,"r") as algo:
        for i in algo:
            print(i[:-1])

def contar(nombre):
    #Cuenta la cantidad de renglones del archivo
    a=0
    with open(nombre,"r") as algo:
        for i in algo:
            a=a+1
    return a

def primerasnlineas(nombre,n):
    with open(nombre,"r") as algo:
        for i in algo[0:n+1]:
            print(i)
def adjuntar(nombre,renglones):
    #Adjunta renglones a un archivo existente"
    with open(nombre,"a") as algo:
        for i in renglones:
            algo.write(str(i) + "\n")
renglones=["hola", "adios","que onda"]
nombre= "fibonacci"

def archivolista(nombre):
    #Devuelve una lista con lo que dice cada renglon de un archivo
    lista=[]
    with open(nombre,"r") as algo:
        for i in algo:
            lista.append(i)
    return lista

def copiararchivo(archivoleer, archivoescribir):
    #Copiar lo de archivo leer en archivo escribir
    archivoescribir2=open(archivoescribir,"w")
    with open(archivoleer,"r") as algo:
        for i in algo:
            archivoescribir2.write(i)
    archivoescribir2.close()

def contarcaracter(nombre, caracter):
    #Cuenta cuantas veces aparece un caracter en un archivo
    a=0
    with open(nombre,"r") as algo:
        for i in algo:
            for j in i:
                if caracter==j:
                    a=a+1
    return a

###################################################
def tablamultiplicar(nombre,n):
    #Hace la tabla de multiplicar de n
    with open(nombre, "w") as algo:
        for i in range(1,11):
            a=n*i
            a=str(a)
            algo.write(str(n) + " "+ "x" + " "+ str(i)+ " " + "= "+ a + "\n")
            #Tambien se puede hacer con un f cadena
n=3
####################################################
# def creartrablasmultiplicar(prefijo):
#     for i in range(1,11):
#         with open(f"({prefijo}_{i}.txt)","w") as algo:
#             for j in range(1,11):
#                 algo.write(f"({i} x {j} = {j*i})" + "\n")
#             #Tambien se puede hacer con un f cadena
# prefijo= "Tabla"
# print(creartrablasmultiplicar(prefijo))

##################################################
# def partidosganados(mundial):
#     ganados=0
#     perdidos=0
#     empate=0
#     numero=" "
#     golfavor=0
#     golencontra=0
#     with open(mundial,"r", encoding = "utf-8") as algo:
#         for i in algo:
#             for j in i:
#                 if j.isdigit():
#                     numero=numero + j
#                     print(numero)
#             if int(numero[0])>int(numero[-1]):
#                 ganados=ganados+1
#             elif int(numero[0])<int(numero[-1]):
#                 perdidos=perdidos +1
#             else:
#                 empate=empate+1
#             golfavor=golfavor+int(numero[0])
#             golencontra=golencontra+int(numero[-1])
#             numero= " "
#     return ganados,perdidos,empate,golfavor,golencontra
# mundial="fibonacci"
# print(partidosganados(mundial))

#################################
archivo = open('animales.csv', 'w')
archivo.write('Nombre;Especie;Edad\n')
archivo.write('Canela;Perro;5\n')
archivo.write('Pelusa;Gato;3\n')
archivo.write('Aurelio;Tortuga;14\n')
archivo.close()

##################################
def leernombres(nombre):
    dic={}
    a=0
    listo=[]
    with open(nombre,"r") as algo:
        for i in algo:
            if a==0:
                b=i.split(";")
            else:
                c=i.split(";")
                for j in range(len(c)):
                    dic[b[j].strip]=c[j].strip()
            listo.append(dic)
            a=a+1
            dic={}
    return listo
nombre='animales.csv'
print(leernombres(nombre))
