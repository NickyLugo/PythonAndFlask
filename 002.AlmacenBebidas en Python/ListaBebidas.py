class AlmacenDeBebidas:
    def __init__(self, idB):
        self.bebida = {
            'id_bebida': idB,
        }

def agregar_bebida():
    bebidas = []
    while True:
        id_bebida = int(input("Ingrese el ID de la bebida: "))
        bebida_nueva = AlmacenDeBebidas(id_bebida)
        bebidas.append(bebida_nueva)

        opcion = input("¿Desea agregar otra bebida? (s/n): ")
        if opcion.lower() != "s":
            break

    return bebidas

lista_bebidas = agregar_bebida()

print("Lista de bebidas ingresadas:")
for bebida in lista_bebidas:
    print(bebida.bebida)