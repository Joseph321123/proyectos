class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    #Indicar que no se haga nada en este momento
    pass
#variable del constructo vacio de la clase
mi_personaje = Personaje() 
mi_personaje.nombre = "ChemaFighter"
mi_personaje.fuerza = 30
mi_personaje.inteligencia = 12
mi_personaje.defensa = 27
mi_personaje.vida= 100

print("El nombre del personaje es ", mi_personaje.nombre)
print("La fuerza del personaje es ", mi_personaje.fuerza)
print("el nombre del personaje es ", mi_personaje.inteligencia)
print("el nombre del personaje es ", mi_personaje.defensa)
print("el nombre del personaje es ", mi_personaje.vida)