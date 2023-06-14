class AlmacenDeBebidas:
    def __init__(self):
        self.bebidas = []

    def menu(self):
        while True:
            print("------ Menú ------")
            print("1) AltaBD")
            print("2) BajaBD")
            print("3) Consulta")
            print("4) Actualización")
            print("5) Calcula precio promedio")
            print("6) Cantidad de items por marca")
            print("7) Contar registros por clasificación")
            print("8) Salir")
            
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.altaBD()
            elif opcion == "2":
                self.bajaBD()
            elif opcion == "3":
                self.consulta()
            elif opcion == "4":
                self.actualizacionBD()
            elif opcion == "5":
                self.precioPromedio()
            elif opcion == "6":
                self.cantidadItemsPorMarca()
            elif opcion == "7":  
                self.contarRegistrosPorClasificacion()
            elif opcion == "8":
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
            print("No hay registros en la lista para eliminar.")
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
            print("No hay registros en la lista para consultar.")
        else:
            print("Registros en la lista:")
            for bebida in self.bebidas:
                print(f"ID: {bebida[0]}, Nombre: {bebida[1]}, Clasificación: {bebida[2]}, Marca: {bebida[3]}, Precio: {bebida[4]}")

    def actualizacionBD(self):
        if not self.bebidas:
            print("No hay registros en la lista para actualizar.")
        else:
            id_actualizar = int(input("Ingrese el ID del registro que desea actualizar: "))
            encontrado = False

            for i, bebida in enumerate(self.bebidas):
                if bebida[0] == id_actualizar:
                    encontrado = True
                    print(f"ID: {bebida[0]}, Nombre: {bebida[1]}, Clasificación: {bebida[2]}, Marca: {bebida[3]}, Precio: {bebida[4]}")
                    print("Seleccione el campo que desea actualizar:")
                    print("1) ID")
                    print("2) Nombre")
                    print("3) Clasificación")
                    print("4) Marca")
                    print("5) Precio")
                    opcion_campo = int(input("Elige una opción: "))

                    if opcion_campo == 1:
                        nuevo_id = int(input("Ingrese el nuevo ID: "))
                        self.bebidas[i] = (nuevo_id, bebida[1], bebida[2], bebida[3], bebida[4])
                    elif opcion_campo == 2:
                        nuevo_nombre = input("Ingrese el nuevo nombre: ")
                        self.bebidas[i] = (bebida[0], nuevo_nombre, bebida[2], bebida[3], bebida[4])
                    elif opcion_campo == 3:
                        nueva_clasificacion = input("Ingrese la nueva clasificación: ")
                        self.bebidas[i] = (bebida[0], bebida[1], nueva_clasificacion, bebida[3], bebida[4])
                    elif opcion_campo == 4:
                        nueva_marca = input("Ingrese la nueva marca: ")
                        self.bebidas[i] = (bebida[0], bebida[1], bebida[2], nueva_marca, bebida[4])
                    elif opcion_campo == 5:
                        nuevo_precio = float(input("Ingrese el nuevo precio: "))
                        self.bebidas[i] = (bebida[0], bebida[1], bebida[2], bebida[3], nuevo_precio)
                    else:
                        print("Opción inválida. No se realizará ninguna actualización.")

                    print("Registro actualizado correctamente.")
                    break

            if not encontrado:
                print("No se encontró ningún registro con el ID proporcionado.")

    def precioPromedio(self):
        if not self.bebidas:
            print("No hay registros en la lista para calcular promedio de precios.")
        else:
            cantidad_registros = len(self.bebidas)
            suma_precios = sum(bebida[4] for bebida in self.bebidas)
            promedio_precios = suma_precios / cantidad_registros
            promedio_precios = round(promedio_precios, 2)  # Redondear a dos decimales

            print(f"Cantidad de registros: {cantidad_registros} items")
            print(f"Suma precios: {suma_precios} pesos")
            print(f"El precio promedio es: {promedio_precios} pesos")
    
    def cantidadItemsPorMarca(self):
        if not self.bebidas:
            print("No hay registros en la lista aun.")
        else:
            #marca = input("Ingrese la marca: ") # Sin convertir a minúsculas
            #cantidad = sum(1 for bebida in self.bebidas if bebida[3] == marca)
            #print(f"La cantidad de items de la marca {marca} son {cantidad} items")

            marca = input("Ingrese la marca: ").lower()  # Convertir a minúsculas
            cantidad = sum(1 for bebida in self.bebidas if bebida[3].lower() == marca)
            print(f"La cantidad de items de la marca '{marca}' son: {cantidad} items.")

    def contarRegistrosPorClasificacion(self):
        if not self.bebidas:
            print("No hay registros en la lista aún.")
        else:
            clasificaciones = {}
            for bebida in self.bebidas:
                clasificacion = bebida[2]
                if clasificacion in clasificaciones:
                    clasificaciones[clasificacion] += 1
                else:
                    clasificaciones[clasificacion] = 1

            for clasificacion, cantidad in clasificaciones.items():
                print(f"{clasificacion}: {cantidad} items.")

almacen = AlmacenDeBebidas()
almacen.menu()