#1
def número_de_grupos_alimentarios():
    return 5
print(número_de_grupos_alimentarios())

#resultado: 5
print("------------")
#2
def número_de_ramas_militares():
    return 5
def número_de_días_en_una_semana_silicona_o_lados_del_triángulo():
    return 10
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo() + número_de_ramas_militares())

#Resultado: Error, porque la variable número_de_días_en_una_semana_silicona_o_lados_del_triángulo no está definida.
#Se agregó una definición de 10 a la variable indefinida, para continuar con resultados en los siguientes ejercicios.
#Resultado final: 5, 10.

print("------------")

#3
def número_de_libros_en_espera():
    return 5
    return 10
print(número_de_libros_en_espera())

#Resultado: 5.
print("------------")
#4
def número_de_dedos():
    return 5
    print(10)
print(número_de_dedos())

#Resultado 5.
print("------------")
#5
def número_de_lagos_grandes():
    print(5)
x = número_de_lagos_grandes()
print(x)

#Resultado: 5, none.
print("------------")

#6
def add(b,c):
    return b+c
print(add(1,2) + add(2,3))

#Resultado: arroja error, por lo que hay que hubo que cambiar print por return

print("------------")

#7
def concatenar(b,c):
    return str(b)+str(c)
print(concatenar(2,5))
#resultado: eliminar comillas y arreglar indentación, para corregir errores.

print("------------")

#8

def número_de_océanos_o_dedos_o_continentes():
    b = 100
    print(b)
    if b < 10:
        return 5
    elif b > 10:
        return 7
    else:
        return 10

print(número_de_océanos_o_dedos_o_continentes())

#Resultado: 100
#           7.
#Se agregaron elif b>10: reutrn 7 y else: return 10, en las condicionales, para corregir el error.

print("------------")

#9
def número_de_días_en_una_semana_silicona_o_lados_del_triángulo(b,c):
    if b<c:
        return 7
    else:
        return 14

print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(2,3))
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(5,3))
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo(2,3) + número_de_días_en_una_semana_silicona_o_lados_del_triángulo(5,3))

#Resultado: 7, 14 y 21. (Se ha eliminado el último return).
print("------------")


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#Resultado: 3+5 = 8. return 10 es ignorado.

#11
b = 500
print(b)
def foobar():
    b >= 300
    print(b)
print(b)
foobar()
print(b)

"""
resultado: 
8
500
500
500
500

Además, se ha eliminado ' ="operador de palabra clave from-rainbow" ' para corregir errores.
"""
print("------------")


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

"""
resultado: 
500
500
300
500
"""
print("------------")

#13

b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

"""
resultado: 
500
500
300
300
"""
print("------------")

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

"""
resultado: 
1
3
2
"""

print("------------")

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

"""
resultado: 
1
3
5
10
"""