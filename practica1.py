import random


numero_secreto = random.randint(0,100)
adivinado = False
intentos = 0
cant_max_intentos = 5

print("Bienvenido al juego de adivinar el numero secreo!")

while not adivinado and intentos<=cant_max_intentos:
 entrada = input("Introduce un numero del 1 al 99: ") #castear
 numero = int(entrada)
 if numero == numero_secreto:
  print("Has adivinado el numero secreto!! ")
  adivinado = True
 elif numero < numero_secreto:
  print("el numero es mayor al ingresado")
 else:
  print("el numero es menor al ingresado")

 intentos+=1

 if not intentos < cant_max_intentos:
  print("No has podido adivinar dentro de los 5 intentos")