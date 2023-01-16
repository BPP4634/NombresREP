from nombres import *

def test_leer_frecuencias_nombres(nombres):
    print(f'Se han leídos {len(nombres)} registros.')
    print('Los tres primeros son:',nombres[:3])
    print('Los tres últimos son:',nombres[-3:])

def test_filtrar_por_genero(nombres,genero):
    fpg=filtrar_por_genero(nombres,genero)
    print(f'Hay {len(fpg)} registros de nombres de {genero}, tres de ellos son: {fpg[:3]}')

def test_calcular_nombres(nombres,genero=None):
    cn=calcular_nombres(nombres,genero)
    if genero!=None:
        print(f'Hay {len(cn)} nombres de {genero}, tres de ellos son: {list(cn)[:3]}')
    else:
        print(f'Hay {len(cn)} nombres en total, tres de ellos son: {list(cn)[:3]}')

def test_calcular_top_nombres_de_año(nombres,anyo,limite=10,genero=None):
    ctnda=calcular_top_nombres_de_año(nombres,anyo,limite,genero)
    if genero!=None:
        print(f'Los {limite} nombres más frecuentes del {anyo} del género {genero} son:')
    else:
        print(f'Los {limite} nombres más frecuentes del {anyo} son:')
    for num,c in enumerate(ctnda):
        print('{}º: {}, cuya frecuencia es {}.'.format(num+1,*c))

def test_calcular_nombres_ambos_generos(nombres):
    cnag=calcular_nombres_ambos_generos(nombres)
    print('Los nombres que han sido usados para ambos géneros son:',cnag)

def test_calcular_nombres_compuestos(nombres,genero=None):
    cnc=calcular_nombres_compuestos(nombres,genero)
    if genero!=None:
        print(f'Los nombres compuestos del género {genero} son:')
    else:
        print(f'Todos los nombres compuestos son:')
    print(cnc)

def test_calcular_nombre_mas_frecuente_por_año(nombres,genero=None):
    cnmfpa=calcular_nombre_mas_frecuente_por_año(nombres,genero)
    if genero!=None:
        print(f'Los nombres más frecuentes por año del género {genero} son:')
    else:
        print(f'Los nombres más frecuentes por año son:')
    for c in cnmfpa:
        print('En {}: {}, cuya frecuencia es {}.'.format(*c))

def test_calcular_frecuencia_por_año(nombres,nombre):
    cfpa=calcular_frecuencia_por_año(nombres,nombre)
    print('La frecuencia del nombre',nombre,'a lo largo de los años es:')
    for c in cfpa:
        print('En {}: {}.'.format(*c))

def test_calcular_frecuencia_acumulada(nombres,nombre):
    cfa=calcular_frecuencia_acumulada(nombres,nombre)
    print(f'La frecuencia total del nombre {nombre} es {cfa}.')

def test_calcular_frecuencias_por_nombre(nombres):
    cfpn=calcular_frecuencias_por_nombre(nombres)
    print('La frecuencia de cada nombre es:')
    for c in cfpn:
        print(f'De {c}: {cfpn[c]}.')

def main():
    DATOS=leer_frecuencias_nombres('./data/frecuencias_nombres.csv')
    #Ejercicio 1
    test_leer_frecuencias_nombres(DATOS)
    #Ejercicio 2
    test_filtrar_por_genero(DATOS,'Hombre')
    test_filtrar_por_genero(DATOS,'Mujer')
    #Ejercicio 3
    test_calcular_nombres(DATOS,'Hombre')
    test_calcular_nombres(DATOS,'Mujer')
    test_calcular_nombres(DATOS)
    #Ejercicio 4
    test_calcular_top_nombres_de_año(DATOS,2004,3,'Hombre')
    test_calcular_top_nombres_de_año(DATOS,2004,5,'Mujer')
    test_calcular_top_nombres_de_año(DATOS,2004)
    #Ejercicio 5
    test_calcular_nombres_ambos_generos(DATOS)
    #Ejercicio 6
    test_calcular_nombres_compuestos(DATOS,'Hombre')
    test_calcular_nombres_compuestos(DATOS,'Mujer')
    test_calcular_nombres_compuestos(DATOS)
    #Ejercicio 7
    test_calcular_nombre_mas_frecuente_por_año(DATOS,'Hombre')
    test_calcular_nombre_mas_frecuente_por_año(DATOS,'Mujer')
    test_calcular_nombre_mas_frecuente_por_año(DATOS)
    #Ejercicio 8
    test_calcular_frecuencia_por_año(DATOS,'IKER')
    #Ejercicio 9
    mostrar_evolucion_por_año(DATOS,'IKER')
    #Ejercicio 10
    test_calcular_frecuencia_acumulada(DATOS,'MARIA')
    #Ejercicio 11
    test_calcular_frecuencias_por_nombre(DATOS)
    #Ejercicio 12
    mostrar_frecuencias_nombres(DATOS,20)

if __name__=='__main__':
    main()