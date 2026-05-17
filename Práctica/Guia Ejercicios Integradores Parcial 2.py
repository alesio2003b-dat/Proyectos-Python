def datosdisco(nombre):
    entero=[]
    T0=[]
    Ty=[]
    tmuestra=[]
    x=[]
    L=[]
        
    with open(nombre,"r") as algo:
        for i in algo:
            a=i.strip().split(";")
            L.append((a[1],a[2],a[3]))
    return (L,len(L))

#def tiempodecoccion(T):
#Es facil hacerlo. Hay que hacer un for que recorra coso y le de distintos valores a M con un if

def sueldoconantiguedad(fentrada,fsalida):
    Nombrestodo=[]
    with open(fentrada,"r") as algo:
        for i in algo:
            a=i.strip().split()
            Nombrestodo.append((a[0],a[1],a[2],a[3]))
    Listanueva=[]
    for i in Nombrestodo:
        if int(i[2])/12 > 10:
            a=int(i[3])+int(i[3])*0.12
        if int(i[2])/12 >=5 and int(i[2])/12<10:
            a=int(i[3])+int(i[3])*0.06
        Listanueva.append((i[0],int(i[1]),i[2],a))
    listaordenada= sorted(Listanueva, key= lambda x: x[1], reverse=True)
    with open(fsalida,"w") as algo:
        for i in listaordenada:
            algo.write( str(i[0]) + " " + str(i[1]) + " "+ str(i[2]) + " " + str(i[3]) + "\n")

#sueldoconantiguedad("Datoos.txt", "salida")

def palindromo(palabra):
    palabra.lower()
    if len(palabra)<=1:
        return True
    else:
        r= palabra[0]==palabra[-1] and palindromo(palabra[1:-1])
    return r
# print(palindromo("anitalavalatina"))

def ordenarrec(lista):
    r=[]
    if len(lista)==0:
       r=[]
    else:
        b=min(lista)
        r.append(b)
        lista.remove(min(lista))
        r=r+ ordenarrec(lista)
    return r
lista=[1,3,4,2,3,1,3,5,6,7,2,4]
print(ordenarrec(lista))

    





