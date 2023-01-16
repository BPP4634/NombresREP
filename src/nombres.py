from collections import namedtuple,Counter,defaultdict
from matplotlib import pyplot as plt
import csv

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def leer_frecuencias_nombres(fichero):
    with open(fichero,encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        return [FrecuenciaNombre(int(a),n.strip(),int(fr),g.strip()) for a,n,fr,g in lector]

def filtrar_por_genero(nombres,genero):
    return [n for n in nombres if n.genero==genero]

def filtrar_por_genero_NEW(nombres,genero):
    if genero==None:
        result=nombres
    else:
        result=filtrar_por_genero(nombres,genero)
    return result

def calcular_nombres(nombres,genero=None):
    return {a.nombre for a in filtrar_por_genero_NEW(nombres,genero)}

def calcular_top_nombres_de_año(nombres,anyo,limite=10,genero=None):
    return sorted([(n.nombre,n.frecuencia) for n in filtrar_por_genero_NEW(nombres,genero) if n.año==anyo],key=lambda x:x[1],reverse=True)[:limite]

def calcular_nombres_ambos_generos(nombres):
    return calcular_nombres(nombres,'Mujer')&calcular_nombres(nombres,'Hombre')

def calcular_nombres_compuestos(nombres,genero=None):
    return {n.nombre for n in filtrar_por_genero_NEW(nombres,genero) if " " in n.nombre}

def calcular_nombre_mas_frecuente_por_año(nombres,genero=None):
    aux=defaultdict(list)
    result=[]
    for n in filtrar_por_genero_NEW(nombres,genero):
        aux[n.año]+=[(n.nombre,n.frecuencia)]
    for a in aux:
        result.append((a,*max(aux[a],key=lambda x:x[1])))
    return sorted(result)

def calcular_frecuencia_por_año(nombres,nombre):
    return sorted([(n.año,n.frecuencia) for n in nombres if n.nombre==nombre])

def mostrar_evolucion_por_año(nombres,nombre):
    aux=calcular_frecuencia_por_año(nombres,nombre)
    años, frecuencias=list(zip(*aux))
    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()

def calcular_frecuencia_acumulada(nombres,nombre):
    return sum([n.frecuencia for n in nombres if n.nombre==nombre])

def calcular_frecuencias_por_nombre(nombres):
    result={}
    for n in calcular_nombres(nombres):
        result[n]=calcular_frecuencia_acumulada(nombres,n)
    return result

def calcular_frecuencias_por_nombreALT(nombres):
    result=defaultdict(int)
    for n in nombres:
        result[n.nombre]+=n.frecuencia
    return result

def mostrar_frecuencias_nombres(registros,limite=10):
    nombres, frecuencias=list(zip(*sorted(calcular_frecuencias_por_nombre(registros).items(),key=lambda x:x[1],reverse=True)[:limite]))
    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(limite))
    plt.show()