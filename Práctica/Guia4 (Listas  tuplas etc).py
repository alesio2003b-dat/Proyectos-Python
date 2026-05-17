#Ejercicio 1
# def quitrep(t1):
#     a=0
#     nueva=()
#     for i in t1:
#         for j in range(len(t1)):
#             if i==t1[j]:
#                 a=a+1 #Acá cuenta cuantas veces aparece un elemento
#         if a==1:
#             nueva += (i,)
#         a=0
#     return nueva
# t1=(1,2,2,2,3,4,4,5)
# print(quitrep(t1))

#Ejercicio 2
# def cont(t1,pal):
#     a=0
#     for i in range(len(t1)):
#         if t1[i]==pal:
#             a=a+1
#     return a
# t1=(1,2,2,2,3,4,4,5)
# print(cont(t1,5))

#Ejercicio 3a
# def cont(t1,pal):
#     #Posicion más lejos en la que aparece un número repetido
#     a=0
#     for i in range(len(t1)):
#         if t1[i]==pal:
#             a=a+1
#             pos=i

#     if a>1: #Posicion mas lejos:
#         return(a, pos)

# t1=(1,2,2,2,3,4,4,5)
# print(cont(t1,4))

#Ejercicio 3b
# def cont(t1,pal):
#     #Posicion primera en la que aparece un número repetido
#     a=0
#     for i in range(len(t1)):
#         if t1[i]==pal and a==0:
#             a=a+1
#             pos=i
#         elif t1[i]==pal and a!=0:
#             a=a+1
#     if a>1: #Posicion mas lejos:
#         return(a, pos)

# t1=(1,2,2,2,3,4,4,5)
# print(cont(t1,2))

#Ejercicio 4
# def pares(t1):
#     #Retoma los elementos en posiciones pares de la tupla
#     nueva=()
#     for i in range(len(t1)):
#         if i%2==0:
#             nueva += (t1[i],)
#     return nueva
# t1=(1,2,2,2,3,4,4,5)
# print(pares(t1))

#Ejercicio 5
# def mayor(t1):
#     nueva=(max(t1),min(t1))
#     return nueva
# t1=(1,2,2,2,3,4,4,5)
# print(mayor(t1))

#El ejercicio 6 no lo hice 

#Ejercicio 7
# def combinar(t1,t2):
#     if len(t1)!=len(t2):
#         return None
#     nueva=()
#     for i in range(len(t1)):
#         a=(t1[i],t2[i])
#         nueva += (a,)
#     return nueva
# t1=(1,2,3)
# t2=("a","b","c")
# print(combinar(t1,t2))

#Desde acá hasta donde aparecen lineas de # no sé qué es (Probablemente sean ejemplos de la teoría)
# def Ultimapos(cad,subcad):
#     """Ingrese 2 cadenas no vacías
#     Devuelve la posición de la última vez que se encuentra subcad en cad"""
#     L=len(cad)-1
#     SUBL=len(subcad)-1
#     CAD=""
#     SUBCAD=""
#     for X in range (L):
#         CAD=CAD+cad[L-X]
#     if len(subcad)>1:
#         for Y in range (SUBL):
#             SUBCAD=SUBCAD+subcad[SUBL-Y]
#     else:
#         SUBCAD=subcad
#     EVA=CAD.find(SUBCAD)
#     if EVA==-1:
#         RES=None
#     else:
#         RES=L-EVA
#     if len(subcad)>1:
#         RES=RES-SUBL
#     return RES

# def tupp(t1,t2):
#     if len(t1)>len(t2):
#         long=len (t2)
#         dou=len(t1)
#     else:
#         long=len(t1)
#         dou= len(t2)
#     coinc=[0]
#     for i in range(long):
#         for j in range(dou):
#             if t1[i]==t2[j]:
#                 n=t2[j]
#                 coinc.append(n)
#     coinc.remove(0)


# t1=(1,2,3,4,0,1,3)
# t2=(0,3,2,5,8,7,1)
# print(tupp(t1,t2))


# def intersect(t1,t2):
#     result=()
#     for e in t1:
#         if e in t2:
#             result += (e,)
#     return result
# print(intersect(t1,t2))}
#############################
################################


#################################

###################################

###################################

#################################

#################################
#Preguntar
#Ejercicio 8 (No sé si funciona o no)
# def combinar(*t1):
#     if len(t1)!=len(t1):
#         return None
#     nueva=()
#     for i in t1:
#         for j in range(len(i)):
#            a=i[j]
#            nueva += (a,)
#     return nueva

# t1=(1,2,3)
# t2=("a","b","c")
# t3=(4,5,6)
# print(combinar(t1,t2,t3))

################################
#Ejercicio 9
# def sumalista(lista,a,b):
#     c=sum(lista[a:b+1])
#     return c

#El mismo pero de otra manera
# def sumalista2(lista,a,b):
#     x=0
#     while a<(b+1):
#         x=lista[a] +x
#         a=a+1
#     return x
# e=[1,2,3,4,5,6]
# print(sumalista2(e,2,4))

##############################
#Ejercicio 10
# def encontrarindice(lista,elemento):
#     a=0
#     for i in range(len(lista)):
#         if lista[i] == elemento:
#             a=a+1
#             return i
#     if a==0:
#         return None
# e=[1,2,3,4,5,6]
# print(encontrarindice(e,6))

##############################
#Ejercicio 11
# def combinarcomunes(l1,l2):
#     a=[]
#     b=[]
#     for i in l1:
#         for j in range(len(l2)):
#             if l2[j]==i:
#                 a.append(i)
#     if len(a)>1:
#         return a
#     if len(a)==0:
#         return b
#     return len(b)
# l1=[1,2,3,5]
# l2=[2,3,4]
# print(combinarcomunes(l1,l2))

##############################
#Ejejrcicio 12
# def sumatot(lista):
#     a=[]
#     for i in range(len(lista)):
#         # if i==0:
#         #     a.append(lista[0])
#         # elif i!=0:
#      b=sum(lista[0:i+1])
#      a.append(b)
#     return a
# lis=[1,2,3,4]
# print(sumatot(lis))

##############################
#Ejercicio 13
# def maxmin(lista):
#     a=(max(lista),min(lista))
#     return a

#Lo mismo pero de otra forma:
# def maxmin(lista):
#     maxin=-99999999999 #Preguntar sobre esto
#     minin=99999999999 #Si está bien poner así o no
#     for i in lista:
#         if i>maxin:
#            maxin=i
#         if i<minin:
#             minin=i
#     a=(maxin,minin)
#     return a
# lis=[132,4,39,4,8,9,5,8,1685,3,3,9,78,1,6,778,1,2,6,851,0,-6,-8415,87685]
# print(maxmin(lis))

#############################
#Ejercicio 14
# def separarmasmenos(lista):
#     positivos=[]
#     negativos=[]
#     for i in lista:
#         if i>0:
#             positivos.append(i)
#         elif i<0:
#             negativos.append(i)
#     return positivos,negativos
# lis=[132,4,39,4,8,9,5,8,1685,3,3,9,78,1,6,778,1,2,6,851,0,-6,-8415,87685]
# print(separarmasmenos(lis))

#############################
#Ejercicio 15
def prohibicion(lista,prohibido):
    lnueva=[]
    b=""
    for i in lista:
        a=list(i)
        for j in prohibido:
            if j in a:
                a.remove(j)
        for k in a:
            b=b+k
        lnueva.append(b)
        b=""
    return lnueva
# lista_original = ['Color rojo', 'Naranja#', 'Verde',
# 'Naranja @', 'Blanco']
# lista_cadenas_prohibidas = ['#', 'Color', '@']
# print(prohibicion(lista_original,lista_cadenas_prohibidas))
#FUNCIONOOOOOOOO ESTOY VOLANDO NANANANA       

#############################
#Ejercicio 16
# def promediostd(lista):
#     promedio=sum(lista)/len(lista)
#     std=0
#     for i in lista:
#         std=std+(((i- promedio)**2)/(len(lista)))
#     std=std**(1/2)
#     return promedio,std
# lis=[0,2,8,-2,-3,9]
# print(promediostd(lis))
#############################
#Ejercicio 17
#Lista juegas olimpicos:
# a=[]
# for i in range(1896,2024):
#     a.append(i)
# # print(a)
# def jj00(lista):
#     añosjuegos=[]
#     for i in range(1896,2024,4):
#         añosjuegos.append(i)
#     añosjuegos.remove(1916)
#     añosjuegos.remove(1940)
#     añosjuegos.remove(1944)
#     añosjuegos.insert(añosjuegos.index(2020),2021)
#     añosjuegos.remove(2020)
#     nueva=[]
#     for i in lista:
#         if i in añosjuegos:
#             nueva.append(i)
#     return nueva
# print(jj00(a))
#Cantidad de jjoo en este siglo:
# añosjuegos=[]
# for i in range(1896,2024,4):
#     añosjuegos.append(i)
# añosjuegos.remove(1916)
# añosjuegos.remove(1940)
# añosjuegos.remove(1944)
# for i in range(len(añosjuegos)):
#     if añosjuegos[i] == 2020:
#      pos=i
# añosjuegos.insert(pos,2021)
# añosjuegos.remove(2020)
# print(len(añosjuegos))
# cant=0
# for i in añosjuegos:
#    if i>2001:
#       cant=cant+1
# print(cant)

###########################
#Ejercicio 18
# def intercalado(l1,l2):
#     a=[]
#     if len(l1)==len(l2):
#         for i in range(len(l2)):
#          a.append(l1[i])
#          a.append(l2[i])
#         return a

#     if len(l1)<len(l2):
#         for i in l1:
#           a.append(i)
#         for j in range(len(l2)):
#            a.insert(1+j+l2.index(l2[j]),l2[j])
#         return a
#     if len(l1)>len(l2):
#         for i in l2:
#           a.append(i)
#         for j in range(len(l1)):
#            a.insert(j+l1.index(l1[j]),l1[j])
#         return a

# l1=[1,2,3,4,12,13,14]
# l2=[7,8,9,10,11]
# print(intercalado(l1,l2))

#########################
# Ejercicio 19
# def contar_elementos_comunes(*listas):
#     """Recibe un número variable de listas como argumentos y retorne una lista con los elementos que son comunes a todas las listas"""
#     Indi=len(listas[0])

#     G=0
#     RES=[]

#     for l in listas[0]:
#         for m in range(len(listas)):
#             if l in listas[m]:
#                 G=G
#             else:
#                 G=1
#         if  G==1:
#             G=0
#         else:
#             RES+=[l]
#     return RES

# l1=[0,1,2,3,4,12,13,14]
# l2=[0,7,8,9,10,1,11]
# l3=[0,1,2,3]
# l4=[0,9,18,24,0,1,3]
# print(elementoscomunes(l1,l2,l3,l4))

#Ejericio 20
# def filtrolong(lista,cadenas):
#     palabras=[]
#     for i in range(len(lista)):
#         if len(lista[i])==cadenas:
#             palabras.append(lista[i])
#     return palabras
# lis=["hola","bambu","abc","hooola"]
# print(filtrolong(lis,3))

#####################################
#Ejercicio 21
# def mayor0(lista):
#     cero=[]
#     for i in range(len(lista)):
#         if lista[i]>0:
#             cero.append(lista[i])
#     return cero
# lista=[1,2,3,-5,-6]
# print(mayor0(lista))

#####################################
#Ejercicio 22
# def empiezaterminaigual(lista):
#     igual=[]
#     for i in lista:
#         if i[0]==i[-1]:
#             igual.append(i)
#     return igual
# lista=["virtud","ala","o","reir","peces","leal"]
# print(empiezaterminaigual(lista))

######################################
#Ejercicio 23
# def div3(lista):
#     div=[]
#     for i in range(len(lista)):
#         if lista[i]%3==0:
#             div.append(lista.index(lista[i]))
#     return div
# lista=[3,4,5,6,7,8,9]
# print(div3(lista))

######################################
#Ejercicio 24
# def filtrar(l1,l2):
#     tru=[]
#     a=0
#     if l1<l2:
#         return None
#     for i in l2:
#         if i==True:
#             tru.append(l1[a])
#         a=a+1
#     return tru
# l1=[1,2,3,4,5,6,7,8,10]
# l2=[True,False,True,False,True,True,True,False,True]
# print(filtrar(l1,l2))
######################################
#Ejercicio 25
# def empiezaletra(lista,letra):
#     palabra=[]
#     for i in lista:
#         if i[0] == letra:
#             palabra.append(i)
#     return palabra
# lista=["Hola", "Adios","Hormiga","Hamaca","Perro"]
# print(empiezaletra(lista,"H"))

#######################################
#Ejercicio 26
# def aplicarfuncion(lista,f):
#     a= [f(x) for x in lista]
#     return a
# lista=[1,2,3,4,5]
# f=lambda x: x**2
# print(aplicarfuncion(lista,f))

########################################
#Ejercicio 27
# domino=[(x,y) for x in range(7) for y in range(7) ]
# print(domino)
# cuadrados=[]
# dominos=[]
# for i in domino:
#     a=i[0]**2 + i[1]**2
#     if a not in cuadrados:
#         cuadrados.append(a)
#         dominos.append(i)
# dominos.insert(dominos.index((3, 5)),(3,4))
# print(dominos)

#########################################
#Ejercicio 28
#Preguntar por qué no funciona
# def encontrar(a,b):
#     hola= [str(x) for x in range(a,b+1)]
#     # cadena= list(map(str,hola)) #convierte lista de enteros en lista de numeros str
#     aparicion= 0
#     # print(cadena)
#     for i in hola:
        
#         for j in range(len((i))):
#             if i[j]=="3":
#                 aparicion=aparicion + 1
#     return aparicion
# a=2
# b=100
# print(encontrar(2,100))

#Versión que funciona 
# def encontrar(a,b):
#     hola= [str(x) for x in range(a,b+1)]
#     aparicion= 0
#     for i in hola:
#          if "3" in i:
#               aparicion=aparicion + 1
#     return aparicion
# a=2
# b=100
# print(encontrar(2,100))

####################################
#Hice primero los ejercicios de diccionario y despues de conjuntos (los de conjuntos están más abajo)
#Ejercicio 35
#Diccionarios:
# def armardiccionario(claves,valores):
#     diccionario={}
#     for i in range(len(claves)):
#         diccionario[claves[i]]=valores[i]
#     return diccionario
# claves=["nombre", "edad", "numero favorito"]
# valores= ["Alesio", 20,13]
# print(armardiccionario(claves,valores))

#Ejercicio 37
# def leerdic(diccionario):
#     for i in diccionario:
#         print(i, diccionario[i])
# a={'Alesio': (9, 10, 8), 'Maddi': (5,6,7), 'Maiana': (4, 3), 'Helena': (2, 3, 4, 5)}
# print(leerdic(a))

#####################################
#Ejercicio 38
# def frecuanciafrutas(lista):
#     cantidad=[]
#     frutas=[]
#     diccionario={}
#     a=0
#     #Primero quito las frutas repetidas
#     for i in lista:
#         if i not in frutas:
#             frutas.append(i)
#     for i in frutas:
#         for j in lista:
#             if i==j:
#                 a=a+1
#         cantidad.append(a)
#         a=0
#     for i in range(len(cantidad)):
#         diccionario[frutas[i]]=cantidad[i]
#     return diccionario
# lista=['manzana', 'naranja', 'manzana',
# 'banana', 'naranja', 'manzana', 'pera']
# print(frecuanciafrutas(lista))

#Fruta más repetida:
# def frecuanciamayorfrutas(lista):
#     cantidad=[]
#     frutas=[]
#     a=0
#     #Primero quito las frutas repetidas
#     for i in lista:
#         if i not in frutas:
#             frutas.append(i)
#     for i in frutas:
#         for j in lista:
#             if i==j:
#                 a=a+1
#         cantidad.append(a)
#         a=0
#     mayorcant=max(cantidad)
#     return frutas[cantidad.index(mayorcant)]

# lista=['pera', 'frutilla', 'ciruela',
# 'banana', 'ciruela', 'durazno', 'frutilla',
# 'ciruela']
# print(frecuanciamayorfrutas(lista))
################################################
#Ejercicio 29

# s1={1,2,3,4}
# s2={3,4,5,6}
# s1.add(0)
# # print(s1)
# s2.update([7,8])
# s2.discard(8)
# # print(s2)
# s3=s1.union(s2)
# s4=s1.intersection(s2)
# s5=s1-s2
# # print(s3)
# # print(s4)
# # print(s5)
# # print(s4<=s1) #Subconjunto
# # print(s5<=s2)
# #print(5 in s4) #Un valor en el conjunto
# #print(max(s3)) #Valor maximo
# #print(len(s4)) #Longitud del conjunto
################################################
#Ejercicio 30
# def encontrarpares(nums,valor):
#     lista=[]
#     conjunto=set()
#     print(type(conjunto))
#     for i in nums:
#         for j in nums:
#             if i+j==valor:
#                 conjunto.update([i,j])
#                 lista.append(conjunto)
#             conjunto=set()
#     return lista
# nums=[1,2,3,4,5]
# valor=5
# print(encontrarpares(nums,valor))

###############################################
#Ejercicio 31
# def quitarrepetidos(lista):
#     norepetidos=[]
#     for i in lista:
#         if i not in norepetidos:
#             norepetidos.append(i)
#     return norepetidos
# lista=[1,2,3,4,5,5,1,2,3]
# print(quitarrepetidos(lista))

#############################################
#Ejercicio 32
# def palabrasunicas(cadena):
#     lista=cadena.split()
#     unicas=set()
#     for i in lista:
#         if i not in unicas:
#             unicas.add(i)
#     return  unicas
# cadena="Hola Hola Hola que están haciendo gente que tal"
# print(palabrasunicas(cadena))

############################################
#33 HACER
#(no lo hice)

############################################
#Ejercicio 34
# def isograma(palabra):
#     letras=[]
#     for i in range(len(palabra)):
#         if palabra[i] not in letras:
#             letras.append(palabra[i])
            
#     if len(letras)!= len(palabra):
#         return False
#     elif len(letras)==len(palabra):
#         return True
# palabra="hola"
# print(isograma(palabra))

# def f(x):
#     def g():
#         x = "abc"
#         print("x =", x)
#     def h():
#         z = x
#         print("z =", z)
#     x = x + 1
#     print("x =", x)
#     h()
#     g()
#     print("x =", x)
#     return g    
# x=3
# z = f(x)
# print("x =", x)
# print("z =", z)
# z()

#######################################
#Ejercicio 39
# def almacenarnotas(alumnos, notas):
#     diccionario={}
#     for i in range(len(alumnos)):
#         diccionario[alumnos[i]]=notas[i]
#     return diccionario
# alumnos=["Alesio","Maddi","Maiana","Helena"]
# notas=[(9,10,8),(5,6),(4,3),(2,3,4,5)]
# a=almacenarnotas(alumnos,notas)

# #a={'Alesio': (9, 10, 8), 'Maddi': (5,6,7), 'Maiana': (4, 3), 'Helena': (2, 3, 4, 5)}
# def trabajodiccinario(a):
#     nuevo={}
#     promedio=[]
#     c=0
#     d=0
#     for i in a:
#       nuevo[i]=sum(a[i])/len(a[i])
#     return nuevo
# print(trabajodiccinario(a))
# b=trabajodiccinario(a)

# def devolvernotprom(nombre):
#     for i in a:
#         if i==nombre:
#             c=a[i]
#             d=b[i]
#     return c,d

# print(devolvernotprom("Alesio"))

# def promediooo(alumnos,notas):
#     promedio=[]
#     dovolucion={}
#     for i in notas:
#         promedio.append(sum(i)/len(i))
#     for i in range(len(alumnos)):
#         dovolucion[alumnos[i]]=promedio[i]
#     return dovolucion
# alumnos=["Alesio","Maddi","Maiana","Helena"]
# notas=[(9,10,8),(5,6),(4,3),(2,3,4,5)]
# print(promediooo(alumnos,notas))

###################################################

###################################################
#Ejercicio 40
# def Diccuad(n):
#     #"""Funcion que recibe un numero y hace lo que hace"""
#     vector=[]
#     for i in range(0,n+1):
#         vector.append(i)
#     dic={}
#     for i in vector:
#         dic[i]=vector[i]**2
#     return dic
# print(Diccuad(5))

#Ejercicio 41
# def contarletras(palabra):
#     letra=[]
#     for i in range(len(palabra)):
#         if palabra[i] not in letra:
#             letra.append(palabra[i])
#     numero=[]      
#     a=0  
#     for i in letra:
#         for j in palabra:
#             if i==j:
#                 a=a+1
#         numero.append(a)
#         a=0
#     diccionario={}
#     for i in range(len(letra)):
#         diccionario[letra[i]]=numero[i]
#     return diccionario
# print(contarletras("palabra"))

###########################################
#Ejercicio 42
#Cartas
# def cartas(lista):
#     """Agrupa palos y cartas"""
#     palos=[]
#     for i in lista:
#         if i[0] not in palos:
#             palos.append(i[0])
#     numeros=[]
#     doblelista=[]
#     for j in palos:
#         for h in lista:
#             if j==h[0]:
#                 numeros.append(h[1])
#         doblelista.append(numeros)
#         numeros=[]
#     dic={}
#     for k in range(len(palos)):
#         dic[palos[k]]=doblelista[k]
#     return dic
# lista=[("oro",3),("basto",5), ("copa",7), ("oro",9),("basto",9), ("copa", 12)]
# print(cartas(lista))

#Ejercicio 43
#Gastos
# def gastos(listagastos):
#     """Da los gastos"""
#     rubros=[]
#     for i in listagastos:
#         if i[0] not in rubros:
#             rubros.append(i[0])
#     gasto=[]
#     total=0
#     for j in rubros:
#         for h in listagastos:
#             if j==h[0]:
#                 total=total+h[1]
#         gasto.append(total)
#         total=0
#     dic={}
#     for k in range(len(rubros)):
#         dic[rubros[k]]=gasto[k]
#     return dic
# lista=[("salud",10),("trabajo",90),("impuesto",25),("impuesto",85),("trabajo",90),("salud",75),("salud",45)]
# print(gastos(lista))
