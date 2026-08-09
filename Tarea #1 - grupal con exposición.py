
import os
from collections import deque

class Producto:
    # Atributos del producto del Nodo
    def __init__(self, codigo, nombre, precio, pais, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.pais = pais
        self.existencia = existencia


    def __str__(self):
        return f"""
        > > Codigo:       {self.codigo}
        > > Nombre:       {self.nombre}
        > > Precio:       {self.precio}
        > > País:         {self.pais}
        > > Existencia:   {self.existencia}
        """

class Nodo_doble:
    # atributos del Nodo (previous, actual, next)
    def __init__(self, contenido):
        self.data = contenido
        self.next = None
        self.prev = None


class lista_doble_enlazada:
    # atributos de la lista doblemente enlazada
    def __init__(self):
        self.head = None

    # ---------------------------------------------------------
    # INSERTAR AL FINAL
    # ---------------------------------------------------------

    def insertar_final(self, contenido):

        nuevo = Nodo_doble(contenido)

        # Lista vacia
        if self.head is None:
            self.head = nuevo
            print(" >> Se ha insertado el producto al final de la lista.")
            return

        actual = self.head

        # Recorrer hasta el ultimo nodo
        while actual.next is not None:
            actual = actual.next

        # Conectar el ultimo nodo con el nuevo
        actual.next = nuevo
        nuevo.prev = actual

        print(" >> Se ha insertado el producto al final de la lista.")


    # ---------------------------------------------------------
    # INSERTAR AL INICIO
    # ---------------------------------------------------------

    def insertar_inicio(self, contenido):

        nuevo = Nodo_doble(contenido)

        # Si la lista no esta vacia
        if self.head is not None:
            nuevo.next = self.head
            self.head.prev = nuevo

        # El nuevo nodo se convierte en el primero
        self.head = nuevo

        print(" >> Se ha insertado el producto al inicio de la lista.")


    # ---------------------------------------------------------
    # INSERTAR EN EL MEDIO
    # ---------------------------------------------------------

    def insertar_medio(self, contenido):

        # Lista vacia
        if self.head is None:
            print(" >> La lista esta vacia. Se ha insertado al inicio.")
            self.insertar_inicio(contenido)
            return

        # Lista con un solo elemento
        if self.head.next is None:
            print(" >> La lista tiene un solo elemento. Se ha insertado al final.")
            self.insertar_final(contenido)
            return

        # Contar cuantos elementos hay
        contador = 0
        actual = self.head

        while actual is not None:
            actual = actual.next
            contador += 1

        mitad = contador // 2

        # Insertar en la posicion de la mitad
        self.insertar_posicion(mitad, contenido)


    # ---------------------------------------------------------
    # INSERTAR EN UNA POSICION
    # ---------------------------------------------------------

    def insertar_posicion(self, posicion, contenido):

        # Si la posicion es 0
        if posicion == 0:
            self.insertar_inicio(contenido)
            print(" >> Se ha insertado el producto en la posicion 0.")
            return

        nuevo = Nodo_doble(contenido)

        actual = self.head
        contador = 0

        # Buscar la posicion
        while actual is not None and contador < posicion:
            actual = actual.next
            contador += 1

        # Posicion fuera de rango
        if actual is None:
            print(" >> Posicion fuera de rango. No se inserto el producto.")
            return

        # Guardar el nodo anterior
        anterior = actual.prev

        # Conectar anterior con nuevo
        anterior.next = nuevo
        nuevo.prev = anterior

        # Conectar nuevo con actual
        nuevo.next = actual
        actual.prev = nuevo

        print(" >> Se ha insertado el producto en la posicion.", posicion)


    # ---------------------------------------------------------
    # ELIMINAR AL INICIO
    # ---------------------------------------------------------

    def eliminar_inicio(self):

        # Lista vacia
        if self.head is None:
            print(" >> La lista esta vacia.")
            return

        # Si solo hay un elemento
        if self.head.next is None:
            self.head = None
            print(" >> Se ha eliminado el unico producto de la lista.")
            return

        # Mover head al siguiente nodo
        self.head = self.head.next

        # El nuevo primero no tiene anterior
        self.head.prev = None

        print(" >> Se ha eliminado el producto en la posicion 0.")


    # ---------------------------------------------------------
    # ELIMINAR AL FINAL
    # ---------------------------------------------------------

    def eliminar_final(self):

        # Lista vacia
        if self.head is None:
            print(" >> La lista esta vacia.")
            return

        # Lista con un solo elemento
        if self.head.next is None:
            self.head = None
            print(" >> Se ha eliminado el ultimo producto de la lista.")
            return

        actual = self.head

        # Buscar el ultimo nodo
        while actual.next is not None:
            actual = actual.next

        # El nodo anterior deja de apuntar al ultimo
        actual.prev.next = None

        print(" >> Se ha eliminado el ultimo producto de la lista.")


    # ---------------------------------------------------------
    # ELIMINAR EN UNA POSICION
    # ---------------------------------------------------------

    def eliminar_posicion(self, posicion):

        # Lista vacia
        if self.head is None:
            print(" >> La lista esta vacia.")
            return

        # Eliminar el primero
        if posicion == 0:
            self.eliminar_inicio()
            return

        actual = self.head
        contador = 0

        # Buscar la posicion
        while actual is not None and contador < posicion:
            actual = actual.next
            contador += 1

        # Posicion fuera de rango
        if actual is None:
            print(" >> Posicion fuera de rango.")
            return

        # Si es el ultimo
        if actual.next is None:
            self.eliminar_final()
            return

        # Conectar el nodo anterior con el siguiente
        actual.prev.next = actual.next

        # Conectar el nodo siguiente con el anterior
        actual.next.prev = actual.prev

        print(" >> Se ha eliminado el producto en la posicion.", posicion)


    # ---------------------------------------------------------
    # BUSCAR CONTENIDO
    # ---------------------------------------------------------

    def buscar_contenido(self, codigo):

        if self.head is None:
            print(" >> La lista esta vacia.")
            return

        actual = self.head
        posicion = 0

        while actual is not None:

            if actual.data.codigo == codigo:
                print("\n  - - -  Informacion del producto encontrado - - - ")
                print(actual.data.__str__())
                return

            actual = actual.next
            posicion += 1

        print(" >> El codigo no coincide o no existe en la lista.")

    # ---------------------------------------------------------
    # VERIFICAR SI ESTA VACIA
    # ---------------------------------------------------------

    def verificar_vacia(self):

        if self.head is None:
            print("\n >> La lista esta vacia.")
            return

        contador = 0
        actual = self.head

        while actual is not None:
            actual = actual.next
            contador += 1

        print(
            f"\n >> La lista no esta vacia. Tiene {contador} elementos."
        )


    # ---------------------------------------------------------
    # MOSTRAR LISTA DE IZQUIERDA A DERECHA
    # ---------------------------------------------------------

    def display(self):

        actual = self.head
        contador = 0

        print("\n")
        while actual is not None:
            print("| --------------------- ", end=" ")
            print(f"\n  - - - [{contador}] Informacion del producto - - - ")
            print(actual.data.__str__())
            
            
            actual = actual.next
            contador += 1

        print("| --------------------- ", end=" ")
        print("\n  - - - None")


    # ---------------------------------------------------------
    # MOSTRAR LISTA DE DERECHA A IZQUIERDA
    # ---------------------------------------------------------

    
    def display_reversa(self):

        if self.head is None:
            print("\n >> La lista esta vacia.")
            return

        actual = self.head
        

        contador = 0           
        # Ir hasta el ultimo nodo
        while actual.next is not None:
            contador += 1
            actual = actual.next

        # Recorrer hacia atras
        while actual is not None:
            print("| --------------------- ", end=" ")
            print(f"\n  - - - [{contador}] Informacion del producto - - - ")
            print(actual.data.__str__())
            actual = actual.prev
            contador -= 1

        print("| --------------------- ", end=" ")
        print("\n  - - - None")

    def conv_lista_a_cola(self): 
        actual = self.head 
        producto_cola = cola() 

        while actual is not None: 
            if actual.data.existencia == 0: 
                producto_cola.insertar_cola(actual.data) 
            actual = actual.next 
        producto_cola.mostrar()


# ============================================================

class Nodo_simple:
    def __init__(self, data):
        self.data = data
        self.next = None

# guía con el material que la profesor proporciono
class cola: 
    def __init__(self): 
        self._elementos = deque() 

    def insertar_cola(self, contenido): 
        self._elementos.append(contenido) 

    # revisar si se implementa en la tarea
    def eliminar_primero(self): 
        if not self._elementos: 
            raise IndexError("La cola esta vacia") 
        return self._elementos.popleft() 

    # revisar si se implementa en la tarea 
    def mostrar_primero(self): 
        if not self._elementos: 
            raise IndexError("La cola esta vacia") 
        return self._elementos[0] 

    def mostrar(self): 
        contador = 0
        if not self._elementos: 
            print("La cola esta vacia") 
        else: 
            print("Elementos en la cola:") 
            for elemento in self._elementos:
                print("| --------------------- ", end=" ") 
                print(f"\n  - - - [{contador}] Informacion del producto - - - ")
                print(elemento.__str__())
                contador += 1
                
            print("| --------------------- ", end=" ")
            print("\n - - - None") 

# =============================================================
# PROGRAMA PRINCIPAL
# =============================================================

lista = lista_doble_enlazada()

# Insertar algunos datos para probar
lista.insertar_final(Producto(1, "Arroz", 2500, "Mexico", 100))
lista.insertar_final(Producto(2, "Frijoles", 1100, "EEUU", 200))
lista.insertar_final(Producto(3, "Lentejas", 900, "Canada", 300))
lista.insertar_final(Producto(4, "Maiz", 600, "Brasil", 400))
lista.insertar_final(Producto(5, "Trigo", 800, "Argentina", 500))   
lista.insertar_final(Producto(6, "Avena", 700, "Chile", 600))
lista.insertar_final(Producto(7, "Tomates", 800, "Peru", 700))
lista.insertar_final(Producto(8, "Cebolla", 900, "Colombia", 800))
lista.insertar_final(Producto(9, "Papas", 1000, "Ecuador", 900))
lista.insertar_final(Producto(10, "Zanahoria", 1100, "Venezuela", 1000))
lista.insertar_final(Producto(11, "Lechuga", 1200, "Uruguay", 1100))
lista.insertar_final(Producto(12, "Pepino", 1300, "Paraguay", 0))
lista.insertar_final(Producto(13, "Calabaza", 1400, "Bolivia", 0))
lista.insertar_final(Producto(14, "Mayonesa", 1500, "Peru", 0))
lista.insertar_final(Producto(15, "Mostaza miel", 1600, "Chile", 0))

os.system("cls")

# =============================================================
# MENUs
# =============================================================

opcion = True

while opcion:

    print("\n - - - - - - -      MENU      - - - - - - - \n")
    print(" 1. Insertar producto al inicio")
    print(" 2. Insertar producto en el medio")
    print(" 3. Insertar producto al final")
    print(" 4. Insertar producto en una posicion")
    print(" 5. Eliminar un producto en una posicion")
    print(" 6. Eliminar el primer producto")
    print(" 7. Eliminar el ultimo producto")
    print(" 8. Buscar un producto en especifico")
    print(" 9. Verificar tamano de la lista")
    print(" 10. Mostrar la lista (left - right)")
    print(" 11. Mostrar la lista en reversa (right - left)")
    print(" 12. Mostrar la cola de productos sin existencia")
    print(" 0. Salir")
    print("\n- - - - - - - - - - - - - - - - - - - - - - -")

    opcion = int(input("\nOperacion ha realizar: "))

    match opcion:

        case 1:
            print("\n >> Insertar producto al inicio:  ")
            codigo = int(input(" >> Codigo del producto:          "))
            nombre = input(" >> Nombre del producto:          ")
            precio = float(input(" >> Precio del producto:          "))
            pais = input(" >> Pais de origen del producto:  ")
            existencia = int(input(" >> Existencia del producto:      "))
            lista.insertar_inicio(Producto(codigo, nombre, precio, pais, existencia))

        case 2:
            print("\n >> Insertar producto en el medio:  ")
            codigo = int(input(" >> Codigo del producto:            "))
            nombre = input(" >> Nombre del producto:            ")
            precio = float(input(" >> Precio del producto:            "))
            pais = input(" >> Pais de origen del producto:    ")
            existencia = int(input(" >> Existencia del producto:        "))
            lista.insertar_medio(Producto(codigo, nombre, precio, pais, existencia))

        case 3:
            print("\n >> Insertar producto al final:     ")
            codigo = int(input(" >> Codigo del producto:            "))
            nombre = input(" >> Nombre del producto:            ")
            precio = float(input(" >> Precio del producto:            "))
            pais = input(" >> Pais de origen del producto:   ")
            existencia = int(input(" >> Existencia del producto:        "))
            lista.insertar_final(Producto(codigo, nombre, precio, pais, existencia))

        case 4:
            posic = int(
                input("\n >> Posicion en la que desea insertar: ")
            )

            print("\n >> Insertar producto en una posicion:  ")
            codigo = int(input(" >> Codigo del producto:                "))
            nombre = input(" >> Nombre del producto:                ")
            precio = float(input(" >> Precio del producto:                "))
            pais = input(" >> Pais de origen del producto:        ")
            existencia = int(input(" >> Existencia del producto:            "))
            lista.insertar_posicion(posic, Producto(codigo, nombre, precio, pais, existencia))

        case 5:
            posic = int(
                input("\n >> Posicion que desea eliminar: ")
            )

            lista.eliminar_posicion(posic)

        case 6:
            lista.eliminar_inicio()

        case 7:
            lista.eliminar_final()

        case 8:
            codigo = int(input("\n >> Codigo del producto a buscar en la lista:     "))
            lista.buscar_contenido(codigo)

        case 9:
            lista.verificar_vacia()

        case 10:
            lista.display()

        case 11:
            lista.display_reversa()
    
        case 12:
            lista.conv_lista_a_cola()

        case 0:
            opcion = False
            print("\n >> Saliendo del programa...")

        case _:
            print(
                "\n >> Error de operacion. "
                "Observe las opciones disponibles."
            )