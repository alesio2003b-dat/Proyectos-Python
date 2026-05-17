#Acá están las funciones a usar en el script Guia Modulos
def filtrar(tupla, condicion):
    a=()
    for i in tupla:
        if condicion=="par":
            if i%2==0:
                a+=(i,)
    return a

def suma(lista,inicio,fin):
    a=0
    for i in lista[inicio:fin+1]:
        a=a+i
    return a
# #Pereza
#Pereza
#Pereza

def concatenar(texto1,texto2):
    return texto1 + texto2
def reemplazar(texto, buscar, reemplazar):
    return texto.replace(buscar,reemplazar)

def mayuscular(cadena):
    return cadena.upper()
def contarletrar(texto, letra):
    texto.lower()
    a=0
    for i in texto:
        if i==letra:
            a=a+1
    return a
