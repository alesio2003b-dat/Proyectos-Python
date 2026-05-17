#1a
def escribir_renglones(nombre_archivo, renglones):
    with open(nombre_archivo, 'w') as archivo:
        i=0
        for renglon in renglones:
            archivo.write(renglon)
            if i != len(renglones) - 1:
                archivo.write('\n')
            i+=1

escribir_renglones("saludos",['hola mundo,','me llamo matias','adios mundo'])

def leer_imprimir(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        a=archivo.readlines()
    return print(a)

#leer_imprimir("saludos")

def contar_lineas(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        a=archivo.readlines()
    return len(a)

#print(contar_lineas("saludos"))

def mostrar_primeras_n_lineas(nombre_archivo,n):
    with open(nombre_archivo, 'r') as archivo:
        i=0
        while i < n:
            print(archivo.readline())
            i+=1

#mostrar_primeras_n_lineas("saludos",1)

#3
def crear_tablas_multiplicar(prefijo):
    for i in range(10):
        with open(prefijo + "_" + str(i+1)+".txt","w") as archivo:
            for j in range(9):
                archivo.write(str(i+1)+"x"+str(j+1)+"="+str((i+1)*(j+1))+"\n")
            archivo.write(str(i+1)+"x10"+"="+str((i+1)*10))

#crear_tablas_multiplicar("tabla")

#5
archivo = open('animales.csv', 'w')
archivo.write('Nombre;Especie;Edad\n')
archivo.write('Canela;Perro;5\n')
archivo.write('Pelusa;Gato;3\n')
archivo.write('Aurelio;Tortuga;14\n')
archivo.close()

#6
def leer_animales(nombre_archivo):
    L=[]
    D={}
    with open(nombre_archivo,"r") as A:
        linea1=A.readline()
        linea=linea1.replace("\n","")
        linea=linea.rsplit(";")
        for i in A:
            if i!=linea1:
                V=i
                V=V.replace("\n","")
                V=V.rsplit(";")
                for j in range(len(linea)):
                    D[linea[j]]=V[j]
                C=D.copy()
                L.append(C)
    return L

#print(leer_animales("animales.csv"))

#7
def tabla_notas(nombre_archivo, alumnos, parcial_1, parcial_2):
    with open(nombre_archivo + ".csv","w") as A:
        A.write("Nombre;Parcial 1;Parcial 2;Promedio\n")
        for i in range(len(alumnos)):
            A.write(str(alumnos[i])+";"+str(parcial_1[i])+";"+str(parcial_2[i])+";"+str((parcial_1[i]+parcial_2[i])/2)+"\n")
    return

tabla_notas("notas.csv", ["Juan", "María", "Carlos"],[85, 92, 78], [90, 88, 81])