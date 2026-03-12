class Animal:
    def __init__(self,nombre, edad,statura):
        self.nombre = nombre
        self.edad = edad
        self.statura = statura

    def hacer_sonido(self,nombre):
        diccionario_sonidos = {
            "Perro": "Guau",
            "Gato": "Miau",
            "Vaca": "Muu"}
        
        if nombre in diccionario_sonidos:
            return diccionario_sonidos[nombre]
        else:   
            return "Sonido desconocido"




animal = Animal("Perro", 5, "Grande")
print("Nombre:", animal.nombre)
print("Edad:", animal.edad)
print("Statura:", animal.statura)
sonido = animal.hacer_sonido(animal.nombre)
print("Sonido:", sonido)


def saludasA(nombre):
    print(f"Hola, {nombre}!")

def despedidasA(nombre):
    print(f"Adiós, {nombre}!")


saludasA("Mundo")
despedidasA("Mundo")

cambiar_nombre = lambda nombre: f"Nuevo nombre: {nombre}"
print(cambiar_nombre("Gato"))
"Aca hago una prueba para ver como son los feach"

def trabajo(oficio):
    print(f"El humano trabaja como {oficio}.")

trabajo("Ingeniero")

"prueba de rama para poder bajarla"

