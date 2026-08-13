
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
        self.tamano = 0

    # ---------------------------------------------------------
    # INSERTAR AL FINAL
    # ---------------------------------------------------------

    def insertar_final(self, contenido):

        nuevo = Nodo_doble(contenido)

        # Lista vacia
        if self.head is None:
            self.head = nuevo
            self.tamano += 1
            print(" >> Se ha insertado el producto al final de la lista.")
            return

        actual = self.head

        # Recorrer hasta el ultimo nodo
        while actual.next is not None:
            actual = actual.next

        # Conectar el ultimo nodo con el nuevo
        actual.next = nuevo
        nuevo.prev = actual
        self.tamano += 1

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
        self.tamano += 1

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
        self.tamano += 1


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
            self.tamano -= 1
            return

        # Mover head al siguiente nodo
        self.head = self.head.next

        # El nuevo primero no tiene anterior
        self.head.prev = None

        self.tamano -= 1
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
            self.tamano -= 1
            return

        actual = self.head

        # Buscar el ultimo nodo
        while actual.next is not None:
            actual = actual.next

        # El nodo anterior deja de apuntar al ultimo
        actual.prev.next = None
        self.tamano -= 1

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

        self.tamano -= 1
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

        if self.tamano == 0:
            print("\n >> La lista esta vacia.")
            return
        elif self.tamano > 0:
            print(f"\n >> La lista contiene {self.tamano} productos.")
            return

    # ---------------------------------------------------------
    # MOSTRAR LISTA DE IZQUIERDA A DERECHA
    # ---------------------------------------------------------

    def display(self):

        print("\n")
        self.display_recursivo(self.head, 0)


    def display_recursivo(self, actual, contador):

        if actual is None:
            print("| --------------------- ", end=" ")
            print("\n  - - - None")
            return

        print("| --------------------- ", end=" ")
        print(f"\n  - - - [{contador}] Informacion del producto - - - ")
        print(actual.data.__str__())

        self.display_recursivo(actual.next, contador + 1)


    # ---------------------------------------------------------
    # MOSTRAR LISTA DE DERECHA A IZQUIERDA
    # ---------------------------------------------------------

    def display_reversa_recursivo(self, actual, contador):
        # Caso base
        if actual is None:
            print("| --------------------- ", end=" ")
            print("\n  - - - None")
            return


        print("| --------------------- ", end=" ")
        print(f"\n  - - - [{contador}] Informacion del producto - - - ")
        print(actual.data.__str__())

        # Llamada recursiva hacia atrás
        self.display_reversa_recursivo(actual.prev, contador - 1)


    # ---------------------------------------------------------
    # CONVERTIR LISTA A COLA DE PRODUCTOS SIN EXISTENCIA
    # ---------------------------------------------------------

    def conv_lista_a_cola(self): 
        actual = self.head 
        producto_cola = cola() 

        while actual is not None: 
            if actual.data.existencia == 0: 
                producto_cola.insertar_cola(actual.data) 
            actual = actual.next 
        producto_cola.mostrar()

    # ---------------------------------------------------------
    # REPORTE DE LO QUE DEBE RECUPERAR EL SUPERMERCADO
    # ---------------------------------------------------------

    def generar_reporte(self, nombre_archivo="reporte_supermercado.txt"):
        if self.head is None:
            print("\n >> La lista esta vacia. No se genero el reporte.")
            return

        total = 0

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("===============================================\n")
            archivo.write("       REPORTE DEL SUPERMERCADO\n")
            archivo.write("===============================================\n\n")

            actual = self.head

            while actual is not None:
                producto = actual.data

                # Recuperacion = cantidad existente * precio.
                subtotal = producto.existencia * producto.precio
                total += subtotal

                archivo.write(f"Codigo: {producto.codigo}\n")
                archivo.write(f"Producto: {producto.nombre}\n")
                archivo.write(f"Pais: {producto.pais}\n")
                archivo.write(f"Cantidad: {producto.existencia}\n")
                archivo.write(f"Precio unitario: ₡{producto.precio:,.2f}\n")
                archivo.write(f"Total por producto: ₡{subtotal:,.2f}\n")
                archivo.write("-----------------------------------------------\n")

                actual = actual.next

            archivo.write(f"\nTOTAL QUE DEBE RECUPERAR EL SUPERMERCADO: ₡{total:,.2f}\n")

        print(f"\n >> Reporte generado correctamente: {nombre_archivo}")
        print(f" >> Total que debe recuperar el supermercado: ₡{total:,.2f}")


# ============================================================
# LISTA DE FRECUENCIAS POR PAIS
# ============================================================

class Nodo_frecuencia:
    def __init__(self, pais):
        self.pais = pais
        self.frecuencia = 1
        self.next = None


class lista_frecuencias:
    def __init__(self):
        self.head = None

    def agregar_pais(self, pais):
        # Si el pais ya existe, aumenta su frecuencia.
        actual = self.head

        while actual is not None:
            if actual.pais.lower() == pais.lower():
                actual.frecuencia += 1
                return
            actual = actual.next

        # Si el pais no existe, se crea un nuevo nodo.
        nuevo = Nodo_frecuencia(pais)

        if self.head is None:
            self.head = nuevo
            return

        actual = self.head
        while actual.next is not None:
            actual = actual.next

        actual.next = nuevo

    def generar_desde_lista(self, lista):
        actual = lista.head

        while actual is not None:
            self.agregar_pais(actual.data.pais)
            actual = actual.next

    def mostrar(self):
        if self.head is None:
            print("\n >> La lista de frecuencias esta vacia.")
            return

        print("\n - - - FRECUENCIA DE IMPORTACIONES POR PAIS - - -")

        actual = self.head
        while actual is not None:
            print(f" >> Pais: {actual.pais} | Frecuencia: {actual.frecuencia}")
            actual = actual.next

    def pais_mayor_frecuencia(self):
        if self.head is None:
            return None

        mayor = self.head
        actual = self.head.next

        while actual is not None:
            if actual.frecuencia > mayor.frecuencia:
                mayor = actual
            actual = actual.next

        return mayor


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
# SUBMENU: GESTION DE PRODUCTOS
# =============================================================

def submenu_gestion_productos(lista):

    while True:

        print("\n========================================")
        print("        GESTION DE PRODUCTOS")
        print("========================================")
        print(" 1. Insertar producto al inicio")
        print(" 2. Insertar producto en el medio")
        print(" 3. Insertar producto al final")
        print(" 4. Insertar producto en una posicion")
        print(" 5. Eliminar producto en una posicion")
        print(" 6. Eliminar el primer producto")
        print(" 7. Eliminar el ultimo producto")
        print(" 0. Regresar al menu principal")
        print("========================================")

        try:
            opcion = int(input("\nSeleccione una opcion: "))
        except ValueError:
            print("\n >> Debe ingresar un numero.")
            input("\nPresione ENTER para continuar...")
            continue

        if opcion == 0:
            return

        elif opcion == 1:

            print("\n >> Insertar producto al inicio:")

            codigo = int(input(" >> Codigo del producto:           "))
            nombre = input(" >> Nombre del producto:           ")
            precio = float(input(" >> Precio del producto:           "))
            pais = input(" >> Pais de origen del producto:   ")
            existencia = int(input(" >> Existencia del producto:       "))

            producto = Producto(
                codigo,
                nombre,
                precio,
                pais,
                existencia
            )

            lista.insertar_inicio(producto)

        elif opcion == 2:

            print("\n >> Insertar producto en el medio:")

            codigo = int(input(" >> Codigo del producto:            "))
            nombre = input(" >> Nombre del producto:             ")
            precio = float(input(" >> Precio del producto:             "))
            pais = input(" >> Pais de origen del producto:     ")
            existencia = int(input(" >> Existencia del producto:         "))

            producto = Producto(
                codigo,
                nombre,
                precio,
                pais,
                existencia
            )

            lista.insertar_medio(producto)

        elif opcion == 3:

            print("\n >> Insertar producto al final:")

            codigo = int(input(" >> Codigo del producto:            "))
            nombre = input(" >> Nombre del producto:             ")
            precio = float(input(" >> Precio del producto:             "))
            pais = input(" >> Pais de origen del producto:     ")
            existencia = int(input(" >> Existencia del producto:         "))

            producto = Producto(
                codigo,
                nombre,
                precio,
                pais,
                existencia
            )

            lista.insertar_final(producto)

        elif opcion == 4:

            print("\n >> Insertar producto en una posicion:")

            posicion = int(
                input(" >> Posicion en la que desea insertar: ")
            )

            codigo = int(
                input(" >> Codigo del producto:                ")
            )

            nombre = input(
                " >> Nombre del producto:                 "
            )

            precio = float(
                input(" >> Precio del producto:                 ")
            )

            pais = input(
                " >> Pais de origen del producto:         "
            )

            existencia = int(
                input(" >> Existencia del producto:             ")
            )

            producto = Producto(
                codigo,
                nombre,
                precio,
                pais,
                existencia
            )

            lista.insertar_posicion(posicion, producto)

        elif opcion == 5:

            posicion = int(
                input("\n >> Posicion que desea eliminar: ")
            )

            lista.eliminar_posicion(posicion)

        elif opcion == 6:

            lista.eliminar_inicio()

        elif opcion == 7:

            lista.eliminar_final()

        else:

            print("\n >> Opcion no valida.")

        input("\nPresione ENTER para continuar...")


# =============================================================
# SUBMENU: CONSULTAS
# =============================================================

def submenu_consultas(lista):

    while True:

        print("\n========================================")
        print("             CONSULTAS")
        print("========================================")
        print(" 1. Buscar un producto")
        print(" 2. Verificar tamano de la lista")
        print(" 3. Mostrar lista izquierda -> derecha (Met. recursivo)")
        print(" 4. Mostrar lista derecha -> izquierda (Met. recursivo)")
        print(" 5. Mostrar cola de productos sin existencia")
        print(" 0. Regresar al menu principal")
        print("========================================")

        try:
            opcion = int(input("\nSeleccione una opcion: "))
        except ValueError:
            print("\n >> Debe ingresar un numero.")
            input("\nPresione ENTER para continuar...")
            continue

        if opcion == 0:
            return

        elif opcion == 1:

            try:
                codigo = int(input("\n >> Codigo del producto a buscar en la lista: "))
            except ValueError:
                print("\n >> ERROR: Debe ingresar un codigo numerico.")
                return

            lista.buscar_contenido(codigo)

        elif opcion == 2:

            lista.verificar_vacia()

        elif opcion == 3:

            print("\n >> MOSTRANDO LISTA DE IZQUIERDA A DERECHA (met. recursivo)")
            lista.display_recursivo(lista.head, 0)

        elif opcion == 4:

            print("\n >> MOSTRANDO LISTA DE DERECHA A IZQUIERDA (met. recursivo)")
            actual = lista.head
            # Buscar el último nodo
            while actual.next is not None:
                actual = actual.next

            # Iniciar recorrido recursivo desde el último nodo
            lista.display_reversa_recursivo(actual, lista.tamano - 1)

        elif opcion == 5:

            lista.conv_lista_a_cola()

        else:

            print("\n >> Opcion no valida.")

        input("\nPresione ENTER para continuar...")


# =============================================================
# SUBMENU: REPORTES
# =============================================================

def submenu_reportes(lista):

    while True:

        print("\n========================================")
        print("             REPORTES")
        print("========================================")
        print(" 1. Frecuencia de productos por pais")
        print(" 2. Generar reporte de recuperacion")
        print(" 0. Regresar al menu principal")
        print("========================================")

        try:
            opcion = int(input("\nSeleccione una opcion: "))
        except ValueError:
            print("\n >> Debe ingresar un numero.")
            input("\nPresione ENTER para continuar...")
            continue

        if opcion == 0:
            return

        elif opcion == 1:

            frecuencias = lista_frecuencias()

            frecuencias.generar_desde_lista(lista)

            frecuencias.mostrar()

            mayor = frecuencias.pais_mayor_frecuencia()

            if mayor is not None:

                print(
                    f"\n >> El pais con mayor frecuencia de importacion "
                    f"es {mayor.pais}, con "
                    f"{mayor.frecuencia} producto(s)."
                )

        elif opcion == 2:

            lista.generar_reporte(
                "reporte_supermercado.txt"
            )

        else:

            print("\n >> Opcion no valida.")

        input("\nPresione ENTER para continuar...")


# =============================================================
# MENU PRINCIPAL
# =============================================================

def menu_principal(lista):

    while True:

        print("\n========================================")
        print("       SISTEMA DE SUPERMERCADO")
        print("========================================")
        print(" 1. Gestion de productos")
        print(" 2. Consultas")
        print(" 3. Reportes")
        print(" 0. Salir")
        print("========================================")

        try:
            opcion = int(input("\nSeleccione una opcion: "))
        except ValueError:
            print("\n >> Debe ingresar un numero.")
            input("\nPresione ENTER para continuar...")
            continue

        if opcion == 0:

            print("\n >> Saliendo del programa...")
            break

        elif opcion == 1:

            submenu_gestion_productos(lista)

        elif opcion == 2:

            submenu_consultas(lista)

        elif opcion == 3:

            submenu_reportes(lista)

        else:

            print("\n >> Opcion no valida.")

        input("\nPresione ENTER para continuar...")


# =============================================================
# EJECUTAR MENU
# =============================================================

menu_principal(lista)