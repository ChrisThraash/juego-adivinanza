
nombre1 = input("Ingrese el nombre del primer jugador: ")
nombre2 = input("Ingrese el nombre del segundo jugador: ")

jugador1 = input("Hola " + nombre1 +"!! que eliges? piedra, papel o tijera?: ").strip().lower()
jugador2 = input("Hola " + nombre2 + "!! que eliges? piedra, papel o tijera?: ").strip().lower()

condicion1 = jugador1=="piedra" and jugador2=="tijera"
condicion2 = jugador1=="papel" and jugador2=="piedra"
condicion3 = jugador1=="tijeras" and jugador2=="papel"

if jugador1==jugador2:
    print("Ha sido un empate!!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado el ",nombre1)
else:
    print("Ha ganado ",nombre2)