import inspect


class Persona:
    nombre: str
    apellido: str
    edad: int
    dni: str

    def __init__(self, nombre: str, apellido: str, edad: int, dni: str):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def presentarse(self):
        return f"Hola, soy {self.nombre_completo()} y tengo {self.edad} años."


def introspeccion_persona():
    print("Atributos de Persona:")
    for atributo in Persona.__annotations__:
        print(f"- {atributo}")

    print("\nCodigo del metodo presentarse:")
    # El end="" es para que no se imprima el \n al final, si no va tener un \n al final del codigo y otro al lado del print.
    print(inspect.getsource(Persona.presentarse), end="")


def crear_clase_dinamicamente(clase_original, nombre_nueva_clase):
    atributos = {
        "__annotations__": dict(getattr(clase_original, "__annotations__", {})),
        "clase_original": clase_original.__name__,
    }

    for nombre, valor in inspect.getmembers(clase_original, inspect.isfunction):
        if nombre == "__init__" or not nombre.startswith("__"):
            atributos[nombre] = valor

    return type(nombre_nueva_clase, (), atributos)


def ejemplo_clase_dinamica():
    PersonaDinamica = crear_clase_dinamicamente(Persona, "PersonaDinamica")
    persona = PersonaDinamica("Valentin", "Perez", 20, "12345678")

    print("\n\nClase creada dinamicamente:")
    print(PersonaDinamica)

    print("\nAtributos de la clase dinamica:")
    for nombre in vars(PersonaDinamica):
        if not nombre.startswith("__"):
            print(f"- {nombre}")

    print("\nInstancia de la clase dinamica:")
    print(persona.presentarse())


if __name__ == "__main__":
    introspeccion_persona()
    ejemplo_clase_dinamica()
