"""Aventura en la Mazmorra

💡 Proyecto: “Aventura en la Mazmorra”

- Un mini-juego por consola donde el jugador recorre una mazmorra generada aleatoriamente.

    .Objetivos del ejercicio:

        - Practicar clases y objetos (Jugador, Enemigo, Habitacion, Objeto).
        - Usar listas y diccionarios para guardar enemigos, objetos y habitaciones.
        - Trabajar lógica condicional y bucles (while, if, etc.).
        - Introducir un poco de aleatoriedad (random).

    .Requisitos mínimos:
        - El jugador empieza con vida aleatoria.
        - La mazmorra tiene 5 habitaciones, cada una puede contener:
            a) Un enemigo (quita vida)
            b) Un objeto (cura)
            c) Estar vacía.

    .El jugador puede decidir:
        a) Explorar (avanza a otra habitación),
        b) Atacar (si hay enemigo),
        c) Si su vida llega a 0 → muere.
        d) Si llega al final → gana.
        e) Si huye de un enemigo → puede perder vida.

    .Extras:
        a) Añade un sistema de inventario.
"""
import random, os, time, sys

########  Duración del juego
numSalasArecorrer = 5

########  Definición de Objetos, Armas y Clases  ########
tiposArmasInicio = {
    "Espada fragmentada"  : [  3,  50, 100],  #Arma: Daño, %Puntería, %Obtencion 
    "Arco dañado"         : [  3,  50, 100],  #Arma: Daño, %Puntería, %Obtencion
    "Piedras"             : [  3,  50, 100]   #Arma: Daño, %Puntería, %Obtencion
    }

tiposArmas = {
    "Pierna de Wirt"      : [ 20, 100,   1],  #Arma: Daño, %Puntería, %Obtencion
    "Varita"              : [  8,  80,  10],  #Arma: Daño, %Puntería, %Obtencion
    "Excalibur"           : [  8,  80,  10],  #Arma: Daño, %Puntería, %Obtencion
    "Arco Largo"          : [  6,  80,  10],  #Arma: Daño, %Puntería, %Obtencion
    "Espada fragmentada"  : [  3,  50, 100],  #Arma: Daño, %Puntería, %Obtencion 
    "Arco dañado"         : [  3,  50, 100],  #Arma: Daño, %Puntería, %Obtencion
    "Piedras"             : [  3,  50, 100]   #Arma: Daño, %Puntería, %Obtencion
    }

tiposObjetos = {
    "Poción"       : [ 3, 80],  #Objeto, Curación, %Obtención
    "Superpoción"  : [10, 25],  #Objeto, Curación, %Obtención
    }

class Jugador ():

    def __init__(self):
        self.nombre = ""
        self.vida = random.randint(15,20)
        self.inventario = {
            "arma" : "",
            "objetos" : []
        }
    
        self.inventario["arma"] = random.choice(list(tiposArmasInicio.keys()))
        primerItem=list(tiposObjetos.keys())[0]  #Se añade una poción por defecto
        añadirObjetos(self, primerItem)

    def miedica(self):
        self.vida-=1
        print("El miedo que tienes por continuar te hace perder 1 de vida.\n")
        input("Pulsa Enter para continuar...")

    def huir(self, enemigo):
        golpeado=(random.randint(1,3) == 2)
        
        if golpeado:
            print(f"\nHuir de una pelea es de cobardes, {enemigo.nombre} te lanza su {enemigo.inventario['arma']},") 
            print(f"tienes la mala suerte de ser golpead@ por ella y pierdes {(tiposArmas[enemigo.inventario['arma']][0])*2} de vida.\n")
            self.vida -= (tiposArmas[enemigo.inventario['arma']][0])*2
        else:
            print(f"\nHuir de una pelea es de cobardes, {enemigo.nombre} te lanza su {enemigo.inventario['arma']}")
            print(f"tienes la suerte de esquivarla y reirte en su cara.\n")
            input("Pulsa Enter para continuar...")
     
class Enemigo ():

    def __init__(self, name):
        self.nombre = name
        self.vida = random.randint(5,15)
        self.inventario = {
            "arma" : ""
        }

        armaAleatoria(self)

########  Definición de Funciones y Salas  ########
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def statusJugador():
    print(f"""
--------------------------------------------------------
Nombre: {personaje.nombre}
Vida: {personaje.vida}
Arma: {personaje.inventario["arma"]} ({tiposArmas[personaje.inventario['arma']][0]} de daño)
Objetos: {personaje.inventario["objetos"]}
--------------------------------------------------------""") 
    
def statusFight(player, enemigo):
    print(f"""
--------------------------------------------------------
Nombre: {player.nombre}
Vida: {player.vida}
Arma: {player.inventario["arma"]} ({tiposArmas[personaje.inventario['arma']][0]} de daño)
Objetos: {player.inventario["objetos"]}
--------------------------------------------------------
Vs.
--------------------------------------------------------
Nombre: {enemigo.nombre}
Vida: {enemigo.vida}
Arma: {enemigo.inventario["arma"]} ({tiposArmas[enemigo.inventario['arma']][0]} de daño)
--------------------------------------------------------""")

def armaAleatoria(player):
     for arma in tiposArmas:
            if (tiposArmas[arma][2] == 1):
                if (random.randint(1,100) == random.randint(1,100)): #1 Posibilidad entre 100 (1%).
                    player.inventario["arma"] = arma
                    break
            elif (tiposArmas[arma][2] == 10):
                if (random.randint(1,10) == random.randint(1,10)): #1 Posibilidad entre 10 (10%).
                    player.inventario["arma"] = arma
                    break
            elif (tiposArmas[arma][2] == 100): # al ser 100% no hace falta hacer un random, muy random sería hacerlo...
                    player.inventario["arma"] = arma
                    break

def armaAleatoriaCofre(player):
    for arma in tiposArmas:
        if (tiposArmas[arma][2] == 1):
            if (random.randint(1,100) == random.randint(1,100)): #1 Posibilidad entre 100 (1%).
                if tiposArmas[arma][0] > tiposArmas[player.inventario['arma']][0]:
                    print(f"\nHas encontrado un arma mejor, decides quedartelo. ")
                    player.inventario["arma"] = arma
                break
        elif (tiposArmas[arma][2] == 10):
            if (random.randint(1,10) == random.randint(1,10)): #1 Posibilidad entre 10 (10%).
                if tiposArmas[arma][0] > tiposArmas[player.inventario['arma']][0]:
                    print(f"\nHas encontrado un arma mejor, decides quedartelo. ")
                    player.inventario["arma"] = arma
                break
    else:
        limpiar()
        statusJugador()
        print(f"\nNo has encontrado ningún arma.")

    input("Pulsa Enter para continuar...")

def objetoAleatoriaCofre(player):
    for objeto in tiposObjetos:
        if (tiposObjetos[objeto][1] == 80):
            if (random.randint(1,5) > 1): #4 posibilidades entre 5 (80%).
                limpiar()
                statusJugador()
                print(f"\nHas encontrado {objeto}, decides quedartelo. ")
                añadirObjetos(player, objeto)
                break
        elif (tiposObjetos[objeto][1] == 25):
            if (random.randint(1,4) == random.randint(1,4)): #1 Posibilidad entre 4 (25%).
                limpiar()
                statusJugador()
                print(f"\nHas encontrado {objeto}, decides quedartelo. ")
                añadirObjetos(player, objeto)
                break
        else:
            limpiar()
            statusJugador()
            print(f"\nNo has encontrado ningún objeto.")
    
    input("Pulsa Enter para continuar...")
                    
def añadirObjetos(player, newItem):
            
    for objeto in player.inventario["objetos"]:
        nameObjeto = list(objeto.keys())[0]
        if  newItem in objeto:
            objeto[newItem]+=1
            break
    else:
        player.inventario["objetos"].append({newItem:1})

def usarObjetos(player, item):
            
    for objeto in player.inventario["objetos"]:
        if  item in objeto:
            objeto[item]-=1
            player.vida += tiposObjetos[item][0]
            print(f"Has utilizado 1 {item}, te has curado {tiposObjetos[item][0]} puntos de vida.")
            if objeto[item]==0:
                player.inventario["objetos"].remove(objeto)
                print(f"Ya no te queda más cantidad de {item}.")    
            input("Presiona Enter para continuar...")
            break

def listarObjetos(player)->list:
    listaObjetos=[]

    for objeto in player.inventario["objetos"]:
        nombre_objeto = list(objeto.keys())[0]
        listaObjetos.append(nombre_objeto)

    return listaObjetos
  
def salaEnemigo(player):
    enemigoFound=random.choice(list(listaEnemigos))
    listaEnemigos.remove(enemigoFound)
    accion = ""
    while (accion != "huir" and accion != "pelear"):
        limpiar()    
        statusJugador()
        
        print(f"\nTe has encontrado con un enemigo, este enemigo se llama {enemigoFound.nombre}.")
        print(f"Tiene en su poder un arma muy poderosa: {enemigoFound.inventario['arma']}.\n")

        accion = input("¿Que quieres hacer? ¿'Huir' o 'Pelear'? ").lower().strip()

    if accion == "huir":
        player.huir(enemigoFound)
        return
    
    elif accion =="pelear":
        
        limpiar()
        statusFight(player, enemigoFound)
        time.sleep(0.5)

        print("\nInicias la pelea.")
        ataque(player, enemigoFound)
        
        limpiar()
        statusFight(player, enemigoFound)
        ataque(enemigoFound, player)
        accion=""
        while(accion != "huir"):
            limpiar()
            statusFight(player, enemigoFound)
            if player.inventario["objetos"] != []:
                accion = input("¿Que quieres hacer? ¿'Huir', 'Pelear' o usar un 'Objeto'? ").lower().strip()
            else:
                accion = input("¿Que quieres hacer? ¿'Huir' o 'Pelear'? ").lower().strip()
                if accion == "objeto": #En esta casuistica no se puede utilizar objetos, no hagas trampas cobarde
                    accion = ""

            if accion == "huir":
                player.huir(enemigoFound)
                return
            elif accion == "pelear":
                ataque(player, enemigoFound)  
                limpiar()
                statusFight(player, enemigoFound)
                
                if enemigoFound.vida <=0:
                    limpiar()
                    statusJugador()
                    if tiposArmas[enemigoFound.inventario['arma']][0] > tiposArmas[player.inventario['arma']][0]:
                        pickArma=input(f"\nHas matado a {enemigoFound.nombre}. Su arma es mejor, ¿Quieres quedartela? (si/no) ")
                        if pickArma == "si":
                            player.inventario['arma']= enemigoFound.inventario['arma']
                    else:
                        print(f"\nHas matado a {enemigoFound.nombre}. Su arma era peor que la tuya, le das una patada.")
                    input("\nPresiona Enter para continuar...")
                    return
                else:
                    ataque(enemigoFound, player)
                if player.vida <= 0:
                    return
                
            elif accion == "objeto":
                print(f"Tienes {listarObjetos(personaje)}.")
                objetoToUse = ""
                while not any(objetoToUse in obj for obj in personaje.inventario["objetos"]):   #Aquí me ha ayudado ChatGPT, demasiado complejo...
                    objetoToUse = input("¿Qué objeto quieres utilizar? ").capitalize().strip()
                    if not any(objetoToUse in obj for obj in personaje.inventario["objetos"]):
                        print("Ese objeto no existe en el inventario.")
                usarObjetos(personaje, objetoToUse)

def salaVacia(player):
   accion = ""
   while (accion != "s"):    
    limpiar()
    statusJugador()
    accion = input(f"\n¿{personaje.nombre}, estás en una sala vacía, continuar (s/n)? ")
    if (accion == "n"):
        personaje.miedica()
 
def salaObjeto(player):
    limpiar()  
    statusJugador()
    print("""
Avanzas por un pasillo silencioso, iluminado solo por antorchas moribundas...
Al fondo, una sala vacía te recibe con un silencio inquietante.
En el centro, un cofre cubierto de polvo parece esperarte desde hace siglos.
Tu mano tiembla al acercarse a la tapa... lo abres""")
    input("\nPresiona Enter para continuar...")
    opcionEncontrada = random.randint(1,4)
    if opcionEncontrada == 1:
        armaAleatoriaCofre(personaje)
    elif opcionEncontrada == 2:
        objetoAleatoriaCofre(personaje)
    elif opcionEncontrada == 3:
        armaAleatoriaCofre(personaje)
        objetoAleatoriaCofre(personaje)
    elif opcionEncontrada == 4:
        print("En el cofre había una serpiente, va y te muerdes, pierdes 3 de vida. ¿Para que tocas?")
        player.vida -= 3
        input("\nPresiona Enter para continuar...")

def ataque(atacante, atacado):
    print(f"\n{atacante.nombre} lanza un poderoso ataque a {atacado.nombre}")
    if tiposArmas[atacante.inventario["arma"]][1] == 100:
        atacado.vida -= tiposArmas[atacante.inventario["arma"]][0]
        print(f"Has conseguido acertar el golpe, haciendole perder {tiposArmas[atacante.inventario['arma']][0]} puntos de vida.\n")
    elif  tiposArmas[atacante.inventario['arma']][1] == 80:
        golpeado = (random.randint(1,5) > 1) # 4 posibilidades de 5, es decir... un 80%! 
        if golpeado:
            atacado.vida -= tiposArmas[atacante.inventario["arma"]][0]
            print(f"Has conseguido acertar el golpe a {atacado.nombre}, haciendole perder {tiposArmas[atacante.inventario['arma']][0]} puntos de vida.\n")
        else:
            print(f"Has fallado el golpe, {atacado.nombre} se rie de {atacante.nombre} !.\n")
    elif  tiposArmas[atacante.inventario['arma']][1] == 50:
        golpeado = (random.randint(1,2) == 1) # 1 posibilidad de 2, es decir... un 50%! 
        if golpeado:
            atacado.vida -= tiposArmas[atacante.inventario['arma']][0]
            print(f"Has conseguido acertar el golpe a {atacado.nombre}, haciendole perder {tiposArmas[atacante.inventario['arma']][0]} puntos de vida.\n")
        else:
            print(f"Has fallado el golpe, {atacado.nombre} se rie de {atacante.nombre}!.\n")
    
    input("Presiona Enter para continuar...")

########  Creación Jugador y Enemigos  ########        

personaje = Jugador()
enemigo1 = Enemigo("Tom Pepino")
enemigo2 = Enemigo("Alfred")
enemigo3 = Enemigo("Shauron")
enemigo4 = Enemigo("PeggaPig")
enemigo5 = Enemigo("La Parca")

listaEnemigos = [enemigo1, enemigo2, enemigo3, enemigo4, enemigo5]

##############################################################################
##################              COMIENZA EL JUEGO              ###############
##############################################################################

#############
#  SALA 1   #
#############
limpiar()         
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
    celda1 = input(f"\n¿{personaje.nombre}, Tienes el valor de seguir adelante (s/n)? ")
    if (celda1 == "n"):
        personaje.miedica()

salasRecorridas = 0
while (personaje.vida > 0 and salasRecorridas < numSalasArecorrer):

    tipoSala=random.randint(1,3)

    if tipoSala == 1: 
        salaEnemigo(personaje)
    elif tipoSala ==2:
        salaVacia(personaje)
    else:
        salaObjeto(personaje)

    salasRecorridas +=1

### Fin del Juego    
limpiar()
if personaje.vida <= 0:
    personaje.vida = 0
    statusJugador()
    print(f"\n{personaje.nombre}, has muerto. Tu leyenda no será recordada, te jodes.")

if personaje.vida > 0:
    statusJugador()
    print(f"\n{personaje.nombre}, has conseguido sobrevivir a las cinco salas. Tu leyenda puede que sea recordada.")

     



        

