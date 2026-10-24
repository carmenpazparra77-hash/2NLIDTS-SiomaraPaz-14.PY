# 3LLSC-YairGonzalez-13.py : Arbol Binario de Busqueda con menu
# Cada nodo tiene como maximo dos hijos:
#   izquierdo -> valores MENORES que el nodo
#   derecho   -> valores MAYORES que el nodo

class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.izquierdo = None
        self.derecho = None

def CrearNodo(valor):
    nuevoNodo = Nodo(valor)  # Creamos el apuntador de la estructura
    return nuevoNodo

# Inserta el valor bajando por el arbol hasta encontrar un lugar vacio
def AgregarNodo(raiz_ref, valor):
    # raiz_ref es una lista [raiz] para simular Nodo*&
    if raiz_ref[0] is None:
        raiz_ref[0] = CrearNodo(valor)
        return

    actual = raiz_ref[0]
    while True:
        if valor < actual.dato:
            if actual.izquierdo is None:
                actual.izquierdo = CrearNodo(valor)
                return
            actual = actual.izquierdo
        elif valor > actual.dato:
            if actual.derecho is None:
                actual.derecho = CrearNodo(valor)
                return
            actual = actual.derecho
        else:
            print(f"El valor {valor} ya existe, no se agrega")
            return

# Una hoja es un nodo sin hijo izquierdo ni derecho
def MostrarHojas(nodo, contador):
    if nodo is None:
        return
    if nodo.izquierdo is None and nodo.derecho is None:
        print(f"{nodo.dato}  (Direccion: {id(nodo)})")
        contador[0] += 1
        return
    MostrarHojas(nodo.izquierdo, contador)
    MostrarHojas(nodo.derecho, contador)

# Preorden: nodo, izquierdo, derecho
def Preorden(nodo):
    if nodo is None:
        return
    print(nodo.dato, end=" ")
    Preorden(nodo.izquierdo)
    Preorden(nodo.derecho)

# Inorden: izquierdo, nodo, derecho (muestra los valores ordenados)
def Inorden(nodo):
    if nodo is None:
        return
    Inorden(nodo.izquierdo)
    print(nodo.dato, end=" ")
    Inorden(nodo.derecho)

# Postorden: izquierdo, derecho, nodo
def Postorden(nodo):
    if nodo is None:
        return
    Postorden(nodo.izquierdo)
    Postorden(nodo.derecho)
    print(nodo.dato, end=" ")

# Muestra la estructura con sangria y las direcciones de memoria
def ImprimirArbol(nodo, nivel, lado):
    if nodo is None:
        return
    print("    " * nivel, end="")
    print(f"{lado}{nodo.dato} | Direccion: {id(nodo)} | Izq: {id(nodo.izquierdo) if nodo.izquierdo else None} | Der: {id(nodo.derecho) if nodo.derecho else None}")
    ImprimirArbol(nodo.izquierdo, nivel + 1, "I- ")
    ImprimirArbol(nodo.derecho, nivel + 1, "D- ")

# Postorden: se borran primero los hijos y al final el padre
def BorrarArbol(nodo_ref, contador):
    # nodo_ref es [nodo] para simular Nodo*&
    if nodo_ref[0] is None:
        return
    izq_ref = [nodo_ref[0].izquierdo]
    der_ref = [nodo_ref[0].derecho]
    BorrarArbol(izq_ref, contador)
    BorrarArbol(der_ref, contador)
    print(f"Elemento borrado {contador[0]} | Dato: {nodo_ref[0].dato} | Direccion: {id(nodo_ref[0])}")
    contador[0] += 1
    nodo_ref[0] = None

def main():
    raiz = [None]  # Declaracion del puntero inicial - usamos lista para referencia
    opc = -1
    print("Actividad 13 - Arbol Binario de Busqueda\n")
    while opc != 0:
        print("\n_____Menu Principal_____")
        print("1. Ingresar elementos_____")
        print("2. Mostrar hojas__________")
        print("3. Visualizar arbol_______")
        print("0. Salir__________________")
        print("==========================")
        opc = int(input("Seleccione una opcion: "))

        if opc == 1:
            cantidad = int(input("Ingrese la cantidad de elementos a agregar: "))
            if cantidad <= 0:
                print("Cantidad no valida de elementos")
            else:
                for i in range(cantidad):
                    valor = int(input(f"Ingrese el valor {i+1}: "))
                    AgregarNodo(raiz, valor)

        elif opc == 2:
            if raiz[0] is None:
                print("El arbol esta vacio")
            else:
                totalHojas = [0]
                print("Hojas del arbol:")
                MostrarHojas(raiz[0], totalHojas)
                print(f"Total de hojas: {totalHojas[0]}")

        elif opc == 3:
            if raiz[0] is None:
                print("El arbol esta vacio")
            else:
                print("Estructura del arbol (R = raiz, I = izquierdo, D = derecho):")
                ImprimirArbol(raiz[0], 0, "R- ")
                print("\nPreorden:  ", end=""); Preorden(raiz[0]); print()
                print("Inorden:   ", end=""); Inorden(raiz[0]); print()
                print("Postorden: ", end=""); Postorden(raiz[0]); print()

        elif opc == 0:
            print("Borrando arbol antes de salir:")
            contador = [1]
            BorrarArbol(raiz, contador)
            print(f"Total de elementos borrados: {contador[0]-1}")
            print("Saliendo del programa...")
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()
