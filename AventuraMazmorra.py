"""Aventura en la Mazmorra

💡 Proyecto: “Aventura en la Mazmorra”

- Un mini-juego por consola donde el jugador recorre una mazmorra generada aleatoriamente.

    .Objetivos del ejercicio:

        - Practicar clases y objetos (Jugador, Enemigo, Habitacion, Objeto).
        - Usar listas y diccionarios para guardar enemigos, objetos y habitaciones.
        - Trabajar lógica condicional y bucles (while, if, etc.).
        - Introducir un poco de aleatoriedad (random).

    .Requisitos mínimos:
        - El jugador empieza con vida y energía aleatorias.
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
"""
import random, os, time

#Definición 
tiposArmasInicio = {
    "Puños"               : [  3, 100, 100],  #Arma: Daño, Durabilidad, %Obtencion
    "Espada fragmentada"  : [  3,  15, 100],  #Arma: Daño, Durabilidad, %Obtencion 
    "Arco dañado"         : [  3,  15, 100],  #Arma: Daño, Durabilidad, %Obtencion
    "Piedras"             : [  3,  15, 100]   #Arma: Daño, Durabilidad, %Obtencion
    }

tiposArmas = {
    "Pierna de Wirt"      : [ 20, 100,   1],  #Arma: Daño, Durabilidad, %Obtencion
    "Varita"              : [  8, 100,  20],  #Arma: Daño, Durabilidad, %Obtencion
    "Excalibur"           : [  8, 100,  20],  #Arma: Daño, Durabilidad, %Obtencion
    "Arco Largo"          : [  6, 100,  20],  #Arma: Daño, Durabilidad, %Obtencion
    "Puños"               : [  3, 100, 100],  #Arma: Daño, Durabilidad, %Obtencion
    "Espada fragmentada"  : [  3,  15, 100],  #Arma: Daño, Durabilidad, %Obtencion 
    "Arco dañado"         : [  3,  15, 100],  #Arma: Daño, Durabilidad, %Obtencion
    "Piedras"             : [  3,  15, 100]   #Arma: Daño, Durabilidad, %Obtencion
    }

tiposObjetos = {
    "Poción"       : [3, 0, 1],  #Objeto, Curación, Energia, Unidades
    "Super Poción" : [3, 0, 1],  #Objeto, Curación, Energia, Unidades
    "Elixir"       : [0, 3, 1],  #Objeto, Curación, Energia, Unidades
    "Super Elixir" : [0, 5, 1]   #Objeto, Curación, Energia, Unidades
    }

class Jugador ():

    def __init__(self):
        self.nombre = ""
        self.vida = random.randint(10,20)
        self.energia = random.randint(10,20)
        self.inventario = {
            "arma" : "",
            "objetos" : []
        }
    
        self.inventario["arma"] = random.choice(list(tiposArmasInicio.keys()))
    
    def miedica(self):
        self.energia -=1
        print("El miedo que tienes por continuar te hace perder 1 punto de energia.\n")
        input("Pulsa intro para continuar...")

    def huir(self):
        self.energia -=3
        self.vida -=2
        print("Huir es de cobardes, pierdes 2 de vida y 3 de energia.\n")
        input("Pulsa intro para continuar...")

    
        
class Enemigo ():

    def __init__(self):
        self.nombre = ""
        self.vida = random.randint(10,20)
        self.energia = random.randint(10,20)
        self.inventario = {
            "arma" : ""
        }

        for arma in tiposArmas:
            if (tiposArmas[arma][2] == 1):
                if (random.randint(1,100) == 7): #1 Posibilidad entre 100 (1%), 7 porque es el número de la suerte.
                    self.inventario["arma"] = arma
                    break
            elif (tiposArmas[arma][2] == 20):
                if (random.randint(1,5) == 2): #1 Posibilidad entre 5 (20%), 2 por ser parecido al 20.
                    self.inventario["arma"] = arma
                    break
            elif (tiposArmas[arma][2] == 100): # al ser 100% no hace falta hacer un random, muy random sería hacerlo...
                    self.inventario["arma"] = arma
                    break

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def statusJugador():
    print(f"""
--------------------------------------------------
Nombre: {personaje.nombre}    |    Vida: {personaje.vida}    |    Energia: {personaje.energia}
Arma: {personaje.inventario["arma"]}
Objetos: {personaje.inventario["objetos"]}
--------------------------------------------------
""") 

def salaEnemigo(player):
    limpiar()    
    statusJugador()
    enemigoFound=random.choice(list(listaEnemigos))
    listaEnemigos.remove(enemigoFound)
    
    print(f"""
Te has encontrado con un enemigo, este enemigo se llama {enemigoFound.nombre}.
Tiene en su poder un arma muy poderosa: {enemigoFound.inventario["arma"]}.
""")
    accion = input("¿Que quieres hacer? ¿Huyes o Atacas? (h/a)")
    if accion == "h":
        player.huir()
        return
    elif accion =="a":
        enemigoFound.vida -= tiposArmas[player.inventario["arma"]][0]
        

#Definición Jugadores
personaje = Jugador()
#Definición Enemigos (5 max.)
enemigo1 = Enemigo()
enemigo1.nombre = "Tom Ridddlye"

enemigo2 = Enemigo()
enemigo2.nombre = "Alfred"

enemigo3 = Enemigo()
enemigo3.nombre = "Shauron"

enemigo4 = Enemigo()
enemigo4.nombre = "PeggaPig"

enemigo5 = Enemigo()
enemigo5.nombre = "La Parca"

listaEnemigos = [enemigo1, enemigo2, enemigo3, enemigo4, enemigo5]

##############################################################################
##################              COMIENZA EL JUEGO              ###############
##############################################################################

#############
#  SALA 1   #
#############
#limpiar()         
print("""
      Bienvenid@ a Aventura en la Mazmorra       
""")
print("""
Te despiertas en una celda húmeda, con el eco de cadenas en la distancia...
Una puerta oxidada se entreabre... y un frío viento te invita a avanzar.
""")      
personaje.nombre = input("Encuentras un papel en el suelo con tu nombre: ")
celda1 = "n"

while (celda1 != "s"):    
    limpiar()
    statusJugador()
    celda1 = input(f"¿{personaje.nombre}, Tienes el valor de seguir adelante (s/n)? ")
    if (celda1 == "n"):
        personaje.miedica()

tipoSala=random.randint(1,3)

if tipoSala == 1:
    salaEnemigo(personaje)
elif tipoSala ==2:
     salaEnemigo(personaje)#salaObjeto()
else:
     salaEnemigo(personaje)#salaVacia()

     



        

