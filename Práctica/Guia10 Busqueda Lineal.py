#Busqueda Lineal
#El ejercicio 1 y 2 no los hice porque no quise buscar las funciones, pero a ojo por los nombres les diría:
#1) a- orden n, b- orden constante (probablemente 2 o 3), c- orden n, d- orden m x n, e- orden n, f- probablemente sea orden constante (3 o así), g- log2(n)
#2) Estos sí que no sé como se cuenta el orden, perdón

#Ejercicio 3
# def buslin(L,x):
#     for i in range(len(L)):
#         if L[i]==x:
#             return i
#     return -1
# L=[1,2,3,4,5,6,3,1,43,7]
# x=1
# print(buslin(L,x))

#Ejercicio 4
#Cantidad de apariciones
# def cantap(L,x):
#     a=0
#     for i in L:
#         if i==x:
#             a=a+1
#     return a

#Ejercicio 5
#Numero máximo
# def nummax(L):
#     a=-99999999999999999999999
#     for i in L:
#         if a<i:
#             a=i
#     return a
# L=[1,3,4,5,7,3,35,4,2,5]
# print(nummax(L))

#Ejercicio 6
#Lista ordenada
# def ordenada(L):
#     orden=True
#     for i in range(len(L)):
#         if L[i]>L[i+1]:
#             orden=False
#             break
#     return orden
# L=[1,3,4,5,7,9,35,54,80,5]
# print(ordenada(L))

#Ejercicio 7
#Posición del último cer0
# def ultimocero(L):
#     cero=0
#     posceros=[]
#     for i in range(len(L)):
#         if L[i]==0:
#             posceros.append(i)
#     if len(posceros)==0:
#         return -1
#     else:
#         return posceros[-1]
# L=[1,3,4,0,7,9,0,54,0,0]
# print(ultimocero(L))


#################################
#Busqueda Binaria
#Este codigo no es el Problema 8, es lo de abajo.
# def buscar(L,e):
#     def bisec(L,e,bajo,alto):
#         print('bajo:'+str(bajo)+';alto:'+str(alto))
#         if alto==bajo:
#             return L[bajo]==e
#         medio=(bajo+alto)//2
#         if L[medio]==e:
#             return True
#         elif L[medio]>e:
#             if bajo==medio:
#                 return False
#             else:
#                 return bisec(L,e,bajo,medio-1)
#         else:
#             return bisec(L,e,medio+1,alto)
#     if len(L)==0:
#         return False
#     else:
#         return bisec(L,e,0,len(L)-1)
# L=[1,3,4,0,7,9,0,54,0,0]
# e=9
# print(buscar(L,e))

#Ejercicio 8
#Rehecho para que dé la posicion
#Busqueda binaria que da la posicion de un elemento en una lista ordenada
def buscarpos(L,e):
    def bisec(L,e,bajo,alto):
        print('bajo:'+str(bajo)+';alto:'+str(alto))
        if alto==bajo:
            trufols= L[bajo]==e
            if trufols==True:
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
# # L=[0,1,3,4,0,7,9,0,54,0,0]
# # e=3
# # print(buscar(L,e))

#Ejercicio 9
#Donde insertar número
def insertar(Lista,x):
    a=buscarpos(Lista,x)
    #print(a)
    if a!=-1:
        return a
    if a ==-1:
        b=9999999999999999
        for i in Lista: #Lo que hago acá es nuscar el número más cercano en la lista al numero x ingresado en la función
            #print(abs(x-i))
            if abs(x-i)<b:
                #print(abs(x-i))
                b=abs(x-i)
                d=i
        print(d)
        c=buscarpos(Lista,d) #Acá busco la posición del número más cercano que está en la lista
        #print(c)
        if d<x: #Por algún motivo, d siempre es menor que x, entonces siempre va a haber que sumarle 1 a c
            c=c+1
        #print("El numero se podría insertar en la posición: ", c)
        return c
# L=[1,2,3,4,5,6,7,8,9,10]
# x= 5.01
# print(insertar(L,x))

#Ejercicio 10
#Insertar elemnto
def insertarelemento(L,x):
    b=insertar(L,x)
    #print(b)
    if b>=len(L):
        L.append(x)
        return L,b
    if L[b]==x:
        return b
    if L[b]!=x:
        L.insert(b,x)
        if b==0:
            return L,b
        else:
            return L,b+1
# L=[1,2,3,4,5,6,7,8,9,10]
# x= 2
# print(insertarelemento(L,x))
  

#Ejercicio 11
#Funcion que remueve un elemento por busqueda binaria
# def remover(lista,x):
#     a=buscarpos(lista,x)
#     if a==-1:
#         return a
#     if a!=-1:
#         lista.remove(x)
#         return lista,a
# L=[1,2,3,4,5,6,7,8,9,10]
# x= 5
# print(remover(L,x))

#Ejercicio 12
# def juegocajas(n):
#     import random
#     import math
#     a=random.randint(1,n)
#     #a tiene que ser un numero random hecho con random. Preguntar como hacerlo
#     cajas=[x for x in range(n)]
#     i=1
#     print(math.log2(n)+1)
#     while i<= math.log2(n)+1:
#         posusuario= int(input("Elija su posicion de caja: "))
#         if cajas[a]<cajas[posusuario]:
#             print("La caja está a la izquierda de la posicion que eligió")
#         elif cajas[a]>cajas[posusuario]:
#             print("La caja está a la derecha de la posición que eligió")
#         else:
#             print("La caja está en la posición elegida")
#             break
#         i=i+1
        
#         print(i)
#     if i>math.log2(n)+1 and cajas[a]!=cajas[posusuario]:
#         print("El regalo estaba en la posición: ",a)
#     if cajas[a]==cajas[posusuario]:
#         print("Felicitaciones, disfrute su regalo")
# print(juegocajas(50))

#Ejercicio 13
#No lo hice pero mi recomendación es que no se gasten en hacerlo, hagan otro ejercicio
# def juegocajasdificil(m,n):
#     #Preguntar como hacer el cuadrado

#Ejercicio 14
#Encontrar posicion más cercana al número
# def encontrarcerca(lista,x):
#     a=buscarpos(lista,x)
#     if a!=-1:
#         return a
#     if a==-1:
#         b=999999999999999999999999999
#         for i in lista:
#             if abs(x-i)<b:
#                 b=abs(x-i)
#                 c=i
#         posnueva=buscarpos(lista,c)
#         if lista[posnueva]<x:
#             posnueva=posnueva+1
#         return posnueva
# L=[1,2,3,4,5,6,7,8,9,10]
# x=0.000000001
# print(encontrarcerca(L,x))

##############################
#Ordenamiento
#Ejercicio 15
# def listaordenada(lista,reverse=False):
#     if reverse==False:
#         reverse=True
#     elif reverse==True:
#         reverse=False
#     b=sorted(lista,reverse=reverse)
#     return b,lista
# lista=[5,4,3,5,6,2,3,4,6,1]
# reverse=True
# print(listaordenada(lista,reverse))

#Ejercicio 16
# def ordenarporpromedio(lista):
#     b=sorted(lista, key= lambda x: x[0]) #Lo copié mal, en el corchete debería ir -1.
#     return b
# lista= [(1,52,"hola"),(74,43,"holaa"),(17,32,"holaaa")]
# print(ordenarporpromedio(lista)) 

#Ejercicio 17
# oracion= str(input("Ingrese una oración: "))
# a= oracion.split()
# b=sorted(a)
# print(b)
# cadena=""
# for i in b:
#     cadena= cadena + " "+ i
# print(cadena)

#Ejercicio 18
#Ordenar palabras en una lista
# def ordenarlongitud(lista):
#     b=sorted(lista, key=len)
#     return b
# lista=["hola","abecedario","comida","lalala","palabra"]
# print(ordenarlongitud(lista))

#Ejercicio 19
#Ordenar negativos y positivos
# def ordenarnegativopositivo(lista):
#   Lo que digo acá abajo es mucho texto, pero el ejercicio bien hecho está más abajo
#   Me di cuenta que esta función no es´ta bien, tienen que crear una lista que se llame ceros
#   Y meter en esa lista los ceros. Después, en mas y menos creo que tiene que ir revelse=False
#   Y en b tienen que poner b= menos + ceros + mas.
#     pos=[]
#     neg=[]
#     for i in lista:
#         if i<0:
#             neg.append(i)
#         else:
#             pos.append(i)
#     mas=sorted(pos, reverse=True)
#     menos=sorted(neg,key=abs,reverse=True)
#     b=menos+mas
#     return b
# lista=[-5,4,3,5,-6,2,-3,-4,6,1]
# print(ordenarnegativopositivo(lista))

#Lo de arriba pero bien hecho:
def ordenarnegativopositivo(lista):
    pos=[]
    neg=[]
    ceros=[]
    for i in lista:
        if i<0:
            neg.append(i)
        elif i>0:
            pos.append(i)
        else:
            ceros.append(i)
    mas=sorted(pos, reverse=True)
    menos=sorted(neg,key=abs,reverse=True)
    b=menos+ceros+mas
    return b
lista=[-5,4,3,5,0,-6,2,0,-3,-4,6,1,0]
# print(ordenarnegativopositivo(lista))


#Ejercicio 20
#Problema baraja española
# palos=["oro","copa","espada","basto"]
# valores=[1,2,3,4,5,6,7,10,11,12]
# mazo =[(x,y) for x in palos for y in valores]
# import random
# random.shuffle(mazo)
# ordenado=sorted(mazo,key=lambda x: (x[0],-x[1])) #El - al lado del segundo x es para que haga el reverse ahí
# print(ordenado)

#Ejercicio 21
#Distintos
# def distintos(L):
## Se puede hacer mucho más facil haciendo b=set(L), return len(b). Que ahí hace un conjunto y se van los repetidos
#     L.sort()
#     dif=[]
#     a=0
#     for i in range(len(L)):
#         if abs(L[0]-L[i]) not in dif:
#             dif.append(abs(L[0]-L[i]))
#             a=a+1
#     return a
# L=[0,0,0,0,0,0,0,0,0,0,0,1,-1]
# print(distintos(L))

#Ejercicio 22
#Buscar anagramas
# def buscaranagrama(lista,palabra):
#     letras=list(palabra.lower())
#     a=0
#     b=0
#     for i in lista:
#         if len(i)==len(palabra):
#             for j in i.lower():
#                 if j in letras:
#                     letras.remove(j)
#             if len(letras)==0:
#                 b=1
#                 return a
#             else:
#              letras=list(palabra.lower())    
#         a=a+1
#     if b==0:
#         return -1
# lista=["hola","cabaña","habitacion","almohada","amor"]
# palabra="AMOR"
# print(buscaranagrama(lista,palabra))

#Ejercicio 23
#El de las películas
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
#print(Peliculas("mejor_pelicula_Oscars.csv"))


        
            





