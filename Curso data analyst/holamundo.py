#texto ignorado en la ejecucion del programa en python 
"""
Comentario largo de
multiples linea



#---------------------------------
# ejemplo de codigo de python 
#---------------------------------

def mi_funcion():
    pass


#sintaxis de python

#reglas que se deben seguir a la hora de escribir el codigo para que sea valido y pueda seguir interpretado correctamente
#la identacion es el espacio en blanco llamada tabulacion o sangria al comienzo de una linea de codigo 
#el scope / alcance de una estructura no se delimitara por llaves como en otros lenguajes sino atraves de la identacion 



x=5
nombre="Christian"

texto = str(x) # casteo (cambia el tipo de formato de numerico a texto str=string)

print (x)
print(nombre)
print(texto)

lista = [1,2,3] #coleccion ordenada y mutable
tupla = (1,2,3,4) # coleccion ordenada y inmutable
rango = range(0,10) # secuencia inmutable de numeros
#dict (diccionario) coleccion no ordenada de pares clave-valor

diccionario = {
    "nombre":  "Christian",
    "apellido": "Huanca",
    "edad" : 29
    }

#SET TYPES (CONJUNTO)

# set (conjunto) [coleccion no ordenada y mutable de elementos UNICOS (no permite repetir)]
conjunto = {1,2,3,4}

#frozenset (conjunto inmutable)
conjunto_inmutable = frozenset({1,2,3,4})

booleano = True
booleano2 = False

#none / null (nulo)

# noneType (nulo) [representa la ausencia de valor o la no definicion]
nulo = None


#casteo de string a integer

nombre = "Christian"
edad = 26
dni = "39645602"

print(type(nombre))
print(type(dni))
print(type(edad))

print(type(int(edad)))
print(type(str(edad)))
"""""
"""
import random

x = random.randrange(1,10) # devuelve un numero random entre 1 y 10 (no incluye al 10)
print(x)

y = random.random
print(y)

txt = "Hola mundo"
txt2 = """" hola mundo """
"""
print(txt[0])

tamanio = len(txt)
tamanio2 = len(txt2)

print(tamanio)
print(tamanio2)

#las busquedas y la mayoria de los metodos son case sensitive ( osea la mayusculas y minusculas importan)
txt3 = "me encanta la peliculas de star wars cap1 cap2 cap3"
print("star wars" in txt3) # revisa si esta dentro de la cadena de texto
print("jedi" in txt3)
print("jedi" not in txt3)
print(txt[0:10]) # extrae parte de una cadena de texto

#devuelve cadena de texto convertida en minuscula 
txt5 = "HOLA MUNDO JAJAJA"
print(txt5.lower())

#devuelve cadena de texto convertida en mayuscula 
txt9 = "ola a todos"
print(txt9.upper())

# la funcion strip() saca espacios del comienzo y del final

txt10 = "     uy me deje     muchos espacios    "

txt10corregido = txt10.strip()

print(txt10corregido)

horas = 10
clases = 60
txt80 = "El contenido de este curso va a durar {} horas. y tendra {} clases."
print(txt80.format(horas,clases))

#\n salto de linea en  strings cons double o single quote
# \t tabulado 


texto77 = "este texto esta en minuscula tambien cada minuscula"
print(texto77.capitalize()) #convierte el primer caracter en mayuscula
print(texto77.title()) #convierte en mayuscula el primer caracter de cada palabra
print(texto77.count("minuscula")) #cuantas veces se repite la palabra

#operadores aritmeticos 

a=50
b=2

#suma
suma = a + b
#resta
resta = a - b
#multiplicacion 
multiplicacion = a*b
#division 
div = a/b
#division entera
divent = a//b
# % resto o division 
resto = a % b
#exponenciacion
exp = a**b

print(suma)
print(resta)
print(multiplicacion)
print(div)
print(divent)
print(resto)
print(exp)

#operadores de asignacion = 

x=10 
sumatorio = 3
x+=sumatorio #10 + 3
x+=sumatorio #13 + 3
print(x)

# operadores de comparacion 
# ( == )comparar igualdades 
# ( ! ) es la negacion 
# != comparar diferencia

x=5
y=6
z=5

print(x==y)
print(x==z)
print(x<y)
print(y>=z)

#operadores logicos
# and or not 

#operadores de identidad (is)(==) (is not)

a = 5 
b = 4 
c = "texto1"
d = "texto1"

booleano = c is d 

print(booleano)


#operadores de pertenencia 

palabra= "en este texto pondremos algunas tecnologias: python, R,                     Django y TensorFlow"
textoAminuscula = palabra.strip().lower()

print("django" in textoAminuscula)

#condicionales ternarias (if inline)


valor_si_condicion_verdadera if condicion else valor_si_condicion_falsa
    x=10
    resultado = "positivo" if x > 0 else "negativo"
   """
""" x = 10
y = 1
z = -100

resultado = "Positivo" if y>0 else "Negativo"
print(resultado)

#manejo de excepciones 
 try: 
    codigo que puede generar una excepcion

    except tipodeexcep as nombrevariable

    finally 
    codigo que siempre se ejecuta, opcional 
    """

#palabras clave para control de flujo 

#BREAK  corta cuando cumple la condicion
#CONTINUE continua si aun se cumple la condicion
#PASS  no hace nada solo sirve como marcador de posicion VERIFICA QUE ESTE TODO OK 


x=0

if x>0:
    print("es un numero positivo")
elif x<0:
    print("es un numero negativo")
else:
    print("es un cero")

# while 

contador = 0 
limite = 5
sumatoria = 0
while contador<=limite:
    sumatoria+=contador
    contador+=1

print("La suma de los numeros hasta ",limite, " es ", sumatoria )


# for
for i in range(0,100,2):
    print(i)


# con try y except nose rompe el programa (ejemplo division por 0)

a=10
b=0

try: #intenta hacer algo
    resultado = a/b
    print(resultado)
except ZeroDivisionError: # si tiene un error lo maneja
    print("No se puede dividir por cero")
finally: #se ejecuta siempre
    print("sale a pesar de los errores")
