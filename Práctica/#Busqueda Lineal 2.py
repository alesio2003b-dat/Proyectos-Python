#Busqueda binaria
def buscar(L,e):
    def bisec(L,e,bajo,alto):
        print('bajo:'+str(bajo)+';alto:'+str(alto))
        if alto==bajo:
            if L[bajo]==e:
                return bajo
            else:
                return -1
        medio=(bajo+alto)//2
        if L[medio]==e:
            return medio
        elif L[medio]>e:
            if bajo==medio:
                return -1
            else:
                return bisec(L,e,bajo,medio-1)
        else:
            return bisec(L,e,medio+1,alto)
    if len(L)==0:
        return -1
    else:
        return bisec(L,e,0,len(L)-1)
# L=[1,3,4,0,7,9,0,54,0,0]
# e=54
# print(buscar(L,e))

#Dónde insertar elemento
def dondeinsertar(L,x):
    a=buscar(L,x)
    if a!= -1:
        return a
    else:
        b=999999999999999999999999999999999999999999
        for i in L:
            if abs(x-i)<b:
                b=abs(x-i)
                c=i
        d=buscar(L,c)
        if c<x:
            d=d+1
        return d
# L=[1,2,3,4,5,6,7,8,9]
# x=42412
# print(dondeinsertar(L,x))   

#Insertar elemento
def insertar(L,x):
    a=buscar(L,x)
    if a!=-1:
        return a
    else:
        b=dondeinsertar(L,x)
        if b>=len(L):
            L.append(x)
        else:
            L.insert(b,x)
        return L,b
# L=[1,2,3,4,5,6,7,8,9]
# x=-1
# print(insertar(L,x))    

#Remover elemento
def remover(L,x):
    a=buscar(L,x)
    if a!=-1:
        L.remove(L[a])
    return L,a
# L=[1,2,3,4,5,6,7,8,9]
# x=9
# print(remover(L,x))

#Juego de las cajas
def juegocajas(n):
    import random
    import math
    ubicación= random.randint(0,n)
    cajas=[x for x in range(n)]


    elección=int(input("Ingrese la posición de la caja: "))
    i=1 #No sé si empieza en 1 o en 0.
    print(math.log2(n)+1)
    while i<=math.log2(n)+1:
        if elección<ubicación:
            print("La caja se encuentra a la derecha de su posición elegida")
        if ubicación<elección:
            print("La caja se encuentra a la izquierda de la posición elegída")
        if ubicación==elección:
            print("La caja estaba en la posición elegida")
            break
        print(i)
        i=i+1
        
        elección=int(input("Ingrese la posición de la caja: "))
    if ubicación!=elección:
        return "La caja se encontraba en la poscición: " + str(ubicación)
# print(juegocajas(40))

#Ordenar
#Lista ordenada
def listaordenada(L,reverse=False):
    if reverse==False:
        a=True
    if reverse==True:
        a=False
    Lista=sorted(L,reverse=a)
    return Lista
# L=[1,31,19,4,-1,23,0]
# print(listaordenada(L,True))

#Ordenar por promedio
def ordenarpromedio(L):
    orden=sorted(L,key= lambda x: x[-1],reverse=True)
    return orden
# L=[("Alesio",20,10),("Maddi",21,9.5),("Chimuela",5,9.75)]
# print(ordenarpromedio(L))

#Ordenar alfabeticamente palabras de una oración
def ordenaroracion(oracion):
    s=oracion.lower().split()
    lista=sorted(s)
    resultado= " "
    for i in lista:
        resultado=resultado+ " "+i
    return resultado
# print(ordenaroracion("Hola gente como andan soy Alesio"))

#Ordenar por longitud
def ordenarlongitud(L):
    lista=sorted(L,key=len,reverse=False)
    return lista
# L=["Hola", "insectos","araña","puesta del sol","Milan"]
# print(ordenarlongitud(L))

#Ordenar negativos y positivos:
def posneg(L):
    pos=[]
    neg=[]
    for i in L:
        if i>=0:
            pos.append(i)
        else:
            neg.append(i)
    pos.sort()
    neg.sort()
    lista=neg+pos
    return lista
# L=[-1,1,2,4,643,-12,-654,0,0,0,-122,542]
# print(posneg(L))

#Distintos
def distintos(L):
    a=set(L)
    return len(a)
# L=[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3]
# print(distintos(L))

#Anagrama
def buscaranagrama(L,palabra):
    letras=list(palabra.lower())
    a=0
    for i in range(len(L)):
        if len(L[i])==len(palabra):
            for j in L[i]:
                if j in letras:
                    letras.remove(j)
        if len(letras)==0:
            a=1
            return i
        letras=list(palabra.lower())
    if a==0:
        return -1
# L=["rama", "amor", "morado",
# "ramo"]
# print(buscaranagrama(L,"roma"))

def Peliculas(nombre):
    año=[]
    pelicula=[]
    peliculaaño=[]
    h=0
    with open(nombre,"r") as algo:
            for i in algo:
                if h!=0: #Esto del h !=0 lo hago para saltearme la primer linea, porque no sé usar el comando readline o algo así :)
                    i=i.strip().split(",")
                    año.append(i[0])
                    pelicula.append(i[-1])
                    peliculaaño.append((i[0],i[-1]))
                h=h+1
    #Ordenar las peliculas por año
    añorden=sorted(peliculaaño, key=lambda x: x[0])
    print(añorden)
    with open("poraño","w") as algo:
        algo.write("Año" + "," + "Película" + "\n")
        for i in añorden:
            algo.write(str(i[0] + ", "+ str(i[-1]) + " \n"))
    
    #Ordenar peliculas por orden alfabetico
    ordenalf=sorted(peliculaaño, key=lambda x: x[1])
    print(ordenalf)
    with open("poralf","w") as algo:
        algo.write("Año" + "," + "Película" + "\n")
        for i in ordenalf:
            algo.write(str(i[0] + ", "+ str(i[-1]) + " \n"))
    #Ordenar por longitud y año
    ordenlongaño=sorted(peliculaaño, key= lambda x: (len(x[1]), x[0]))
    print(ordenlongaño)
    with open("porlongaño","w") as algo:
        algo.write("Año" + "," + "Película" + "\n")
        for i in ordenlongaño:
            algo.write(str(i[0] + ", "+ str(i[-1]) + " \n"))
print(Peliculas("mejor_pelicula_Oscars.csv"))





    
        