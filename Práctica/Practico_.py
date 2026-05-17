# Ejercicio 1
# Defina una función integral_aprox(f, a, b, n) que toma una función
# f:R->R, dos flotantes a,b y un entero positivo n y devuelve
# el valor aproximado de la integral de f sobre [a,b] usando la formula
# del punto medio:
# - se divide [a,b] en n subintervalos iguales I_i de longitud h
# I = Suma f(m_i) h  con i=1,..,n y m_i el punto medio de I_i
# por ej: integral_aprox(abs, -3, 4, 10) devuelve 12.459999999999999
#         integral_aprox(lambda x: x**3, 2, 5.5, 50) devuelve 224.74954687499977

def integral_aprox(f, a, b, n):
    """Funcion que toma una f:R->R, dos flotantes a,b y un entero positivo n y devuelve el valor aproximado de la integral de f sobre [a,b]"""
    empiezosubint=(b-a)/n
    tupla=()
    intervalos=[]
    for i in range(n):
        if i==0:
            tupla+=(a,a+empiezosubint)
        if i>0 and i!=(n-1):
            tupla+=(a+i*empiezosubint,a+(i+1)*empiezosubint)
        if i==(n-1):
            tupla+=(a+i*empiezosubint,b)
        intervalos.append(tupla)
        tupla=()
    mi=[]
    for i in intervalos:
        d=(i[0]+i[1])/len(i)
        mi.append(d)
        d=0
    I=0
    for i in mi:
        e=f(i)*empiezosubint
        I=I+e
    return I

# Ejercicio 2
# Defina una función estadistica que toma un numero variable de argumentos
# numéricos y devuelve un diccionario con información estadística de estos.
# En particular, contendrá el máximo, el mínimo, la media y la 
# mediana (ordenando los datos el valor del medio si hay un nro impar de datos, o el promedio
# de los dos valores del medio si hay nro par).
# por ej: estadistica(1,3,2) devuelve {'max': 3, 'min': 1, 'media': 2.0, 'mediana': 2}
#         estadistica(7,2,8,10) devuelve {'max': 10, 'min': 2, 'media': 6.75, 'mediana': 7.5}

def estadistica(*args):
    """Funcion que recibe un número variables de argumentos númericos y devuelve un diccionario con información estadística de ellos, como lo es el maximo, minimo, la media y la mediana"""
    estats=[max(args),min(args),sum(args)/len(args)]
    argus=list(args)
    otra=argus
    lista=[]
    a=0
    for i in range(len(argus)):
        lista.append(min(otra[i-a:]))
        otra.remove(min(otra[i-a:]))
        a=a+1
    print(lista)

    if len(args)%2!=0:
        b= lista[int(len(lista)/2)]
        estats.append(b)
    if len(args)%2==0:
        b=(lista[int(len(lista)/2)]+lista[int((len(lista)-1)/2) ])/2
        estats.append(b)
    nonmbres=["max","min","media","mediana"]
    dic={}
    for i in range(len(nonmbres)):
        dic[nonmbres[i]]=estats[i]
    return dic


# # Ejercicio 3
# # Defina una función suma_impares(a) que dada una lista a de números enteros
# # retorne la tupla (s, z) donde s es la suma de los números impares en a y 
# # z es la cantidad de números impares en a.
# # por ej: suma_impares([3, 6, 2, 5, 7]) devuelve (15, 3).
# #         suma_impares([12, 24, 8, 100]) devuelve (0, 0).

def suma_impares(a):
    """"Dada una lista a devuelve una tupla de enteros (s,z) donde s es la suma de los numeros impares en a y z es la cantidad de numeros impares en a"""
    s=0
    cantidad=[]
    z=0
    for i in a:
        if i%2!=0:
            z=z+1
            s=s+i
    return(s,z)



# # Ejercicio 4
# # Defina una función palabras_con_caracter_medio(cadena, carácter) que reciba dos strings:
# # * cadena: una cadena de texto que contiene palabras separadas por espacios.
# # * caracter: un carácter que se utilizará como filtro.
# # La función debe devolver una lista de palabras de la cadena que cumplan con:
# # * La palabra debe contener el carácter en algún lugar de la misma, pero no al principio ni al final.
# # * El carácter no debe ser ni el primer ni el último carácter de la palabra.
# # por ej: palabras_con_caracter_medio('el campo se localiza lejos y la ciudad cerca', 'a') devuelve ['campo', 'ciudad']
# #         palabras_con_caracter_medio('el campo se localiza lejos y la ciudad cerca', 'o') devuelve ['localiza', 'lejos']

def palabras_con_caracter_medio(cadena, caracter):
    """Funcion que recibe dos strings: Una cadena que contiene palabras separadas por espacios y un caracter que se utiliza como filtro
    La funcion devuelve una lista de palabras de la cadena que contienen el caracter en algun lugar de la misma pero no al principio ni al final"""
    espacios=cadena.split()
    nada=0
    sumo=0
    lista=[]
    for i in espacios:
        if i[0]==caracter or i[-1]== caracter: 
            nada=1
        for j in i:
            if j==caracter:
                sumo=sumo+1
        if sumo>=1 and nada==0:
            lista.append(i)
        sumo=0
        nada=0
    return lista
