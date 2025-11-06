"""Aventura en la Mazmorra

💡 Proyecto: “Aventura en la Mazmorra”

- Un mini-juego por consola donde el jugador recorre una mazmorra generada aleatoriamente.

    .Objetivos del ejercicio:

        - Practicar clases y objetos (Jugador, Enemigo, Habitacion, Objeto).
        - Usar listas y diccionarios para guardar enemigos, objetos y habitaciones.
        - Trabajar lógica condicional y bucles (while, if, etc.).
        - Introducir un poco de aleatoriedad (random).

    .Requisitos mínimos:
        - El jugador empieza con vida y energía limitadas.
        - La mazmorra tiene 5 habitaciones, cada una puede contener:
            a) Un enemigo (quita vida)
            b) Un objeto (cura o da energía)
            c) Estar vacía.

    .El jugador puede decidir:
        a) Explorar (avanza a otra habitación),
        b) Atacar (si hay enemigo),
        c) Descansar (recupera energía, pero pasa tiempo).
        d) Si su vida llega a 0 → muere.
        e) Si llega al final → gana.
        f) Si huye de un enemigo → pierde puntos o energía.

    .Extras:
        a) Añade un sistema de inventario.
        b) Guarda las estadísticas de la partida en un archivo .txt.
"""
import random

#Definición 
armas = {
    "Espada fragmentada"  : 3,  #Arma, Daño
    "Arco dañado"         : 3,  #Arma, Daño
    "Piedras"             : 3,  #Arma, Daño
    "Puños"               : 2   #Arma, Daño
    }

objetos = ["Poción", "Super Poción"]

class Jugador ():

    def __init__(self):
        self.nombre = ""
        self.vida = random.randint(5,10)
        self.energia = random.randint(5,10)
        self.inventario = {
            "arma" : "",
            "Objetos" : []
        }
    
        self.inventario["arma"] = random.choice(list(armas.keys()))


        #for objeto in objetos:
        #    if (random.randint(1,5) ==2 ): #20% Posibilidades
        #        self.inventario.append(objeto)


class Enemigo ():

    def __init__(self):
        self.nombre = ""
        self.vida = random.randint(5,10)
        self.energia = random.randint(5,10)
        self.inventario = []


prueba = Jugador()

print(f"{prueba.inventario}")
