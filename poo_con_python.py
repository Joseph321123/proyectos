class Personaje:
    #Atributos de la clase
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    

#constructor de la clase
    def __init__(self, nombre,fuerza,inteligencia,defensa,vida):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida

#para el examen
#que significa "self" (referencia al mismo objeto)
#que es init (constructor que inicializa el atributo del objeto)
#por que empieza con doble guion bajo (por que es un metodo magico, dunder)
# en que momento se ejecuta el metodo init (cunado se crea o construye el objeto)

    def imprimir_atributos(self):
        print("- Nombre: ", self.nombre)
        print("-Fuerza: ",self.fuerza)
        print("-Inteligencia: ",self.inteligencia)
        print("-Defensa: ",self.defensa)
        print("-Vida: ",self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza=self.fuerza+fuerza
        #self.fuerza += fuerza
        self.inteligencia=self.inteligencia+inteligencia
        self.defensa=self.defensa+defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida=0
        print(self.nombre,"ha muerto")
        #return self.vida <=0

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño= self.dañar(enemigo)
        enemigo.vida= enemigo.vida - daño
        print(self.nombre, "ha realizado ", daño, " puntos de daño a", enemigo.nombre)
        print("Vida de ", enemigo.nombre, " es ", enemigo.vida)


class Guerrero(Personaje):

    pass 

tlatoani = Guerrero("Apocalipto", 50, 70, 30, 100)



#variable del constructo  de la clase
# mi_personaje = Personaje("Dante",100,3,70,100) 
# mi_personaje.imprimir_atributos()
# mi_enemigo=Personaje("Vergil",70,30,70,100)
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.imprimir_atributos
#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())



# mi_personaje.subir_nivel(10,1,5)
# print("----------------")
# mi_personaje.imprimir_atributos()
# mi_personaje.nombre = "ChemaFighter"
# mi_personaje.fuerza = 30
# mi_personaje.inteligencia = 12
# mi_personaje.defensa = 27
# mi_personaje.vida= 100

# print("El nombre del personaje es ", mi_personaje.nombre)
# print("La fuerza del personaje es ", mi_personaje.fuerza)
# print("el nombre del personaje es ", mi_personaje.inteligencia)
# print("el nombre del personaje es ", mi_personaje.defensa)
# print("el nombre del personaje es ", mi_personaje.vida)