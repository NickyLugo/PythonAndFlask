class AlmacenDeBebidas:
    def __init__(self):
        self.bebidas = []

    def menu(self):
        while True:
            print("---- Menú ----")
            print("1) AltaBD")
            print("2) BajaBD")
            print("3) Consulta")
            print("4) Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.altaBD()
            elif opcion == "2":
                self.bajaBD()
            elif opcion == "3":
                self.consulta()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

    def altaBD(self):
        id = int(input("Ingrese el ID: "))
        nombre = input("Ingrese el nombre: ")
        clasificacion = input("Ingrese la clasificación: ")
        marca = input("Ingrese la marca: ")
        precio = float(input("Ingrese el precio: "))

        bebida = (id, nombre, clasificacion, marca, precio)
        self.bebidas.append(bebida)
        print("Registro añadido correctamente.")

    def bajaBD(self):
            if not self.bebidas:
              print("No hay registros en la lista.")
            else:
                id_baja = int(input("Ingrese el ID del registro que desea eliminar: "))
                encontrado = False

                for bebida in self.bebidas:
                    if bebida[0] == id_baja:
                        self.bebidas.remove(bebida)
                        encontrado = True
                        print("Registro eliminado correctamente.")
                        break

                if not encontrado:
                    print("No se encontró ningún registro con el ID proporcionado.")

    def consulta(self):
        if not self.bebidas:
            print("No hay registros en la lista.")
        else:
            print("Registros en la lista:")
            for bebida in self.bebidas:
                print(f"ID: {bebida[0]}, Nombre: {bebida[1]}, Clasificación: {bebida[2]}, Marca: {bebida[3]}, Precio: {bebida[4]}")

# Ejemplo de uso
almacen = AlmacenDeBebidas()
almacen.menu()