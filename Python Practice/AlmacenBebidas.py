"""
**Almacén de bebidas**

Objeto:Bebida

Parametros: 
1) id_Bebida
2) nombreBebida
3) clasificacionBebida (ej. Agua, Bebidas Azucaradas, Bebidas energeticas)
4) marcaBebida
5) precioBebida

Operaciones:
alta()
baja()
actualizacion()
mostrar()

Funciones:
A) Calcular Precio promedio de bebidas { ejemplo. precioPromedio = [ sum(precios)/cantidad ] }
B) Cantidad de bebidas de una Marca {Contar marcaBebida}
C) Cantidad por clasificacion {print( "Agua: " + X + ", Bebidas Azucaradas: " + Y ) }
"""

class AlmacenDeBebidas:
    def __init__(self, idB, nombreB, clasificacionB, marcaB, precioB:
        self.bebida = {
            'id_bebida': idB,
            'nombre_bebida': nombreB,
            'clasificacion_bebida': clasificacionB,
            'marca_bebida': marcaB,
            'precio_bebida': precioB
        }

# Crear la lista de bebidas inicial
bebidas = [
    AlmacenDeBebidas(1, 'Agua mineral', 'Agua', 'Peñafiel', 19.00),
    AlmacenDeBebidas(2, 'Coca-Cola', 'Bebida azucarada', 'Coca-Cola', 18.00),
    AlmacenDeBebidas(3, 'Squirt', 'Bebida azucarada', 'Pepsico', 15.00),
    AlmacenDeBebidas(4, 'Sidral Mundet', 'Bebida azucarada', 'Coca-Cola', 16.50),
    AlmacenDeBebidas(5, 'Sangria Señorial', 'Bebida azucarada', 'Mezgo', 19.50),
    AlmacenDeBebidas(6, 'Boing', 'Bebida azucarada', 'Pascual', 12.50),
    AlmacenDeBebidas(7, 'Monster', 'Bebida energetica', 'Monster', 32.50),
    AlmacenDeBebidas(8, 'Suerox', 'Bebida hidratante', 'Genomma Lab.', 20.70),
    AlmacenDeBebidas(9, 'Electrolit', 'Bebida hidratante', 'Pisa', 21.00),
    AlmacenDeBebidas(10, 'Arizona', 'Bebida azucarada', 'Grupo Jumex', 15.00),
    AlmacenDeBebidas(11, 'Juego Manzana', 'Bebida azucarada', 'Del Valle', 15.00),
    AlmacenDeBebidas(12, 'Epura', 'Agua', 'Pepsico', 9.50),
    AlmacenDeBebidas(13, 'Bonafont', 'Agua', 'Bonafont', 11.50),
    AlmacenDeBebidas(14, 'Skarch', 'Agua', 'Embotelladora Aga', 8.00),
    AlmacenDeBebidas(15, 'Delaware Punch', 'Bebida azucarada', 'Coca-Cola', 15.00),
    AlmacenDeBebidas(16, 'Sprite', 'Bebida azucarada', 'Coca-Cola', 16.00),
    AlmacenDeBebidas(17, 'Red Bull', 'Bebida energetica', 'Red Bull', 47.00),
    AlmacenDeBebidas(18, 'Amper', 'Bebida energetica', 'Quala',15.00 ),
    AlmacenDeBebidas(19, 'Vitaminwater', 'Bebida energetica', 'Coca-Cola', 19.50),
    AlmacenDeBebidas(20, 'Vive100', 'Bebida energetica', 'Quala', 14.00),  
]
