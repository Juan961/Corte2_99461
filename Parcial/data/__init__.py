from typing import List

from models import Bebidas, Condimentos, Lacteos


products_bebidas:List[Bebidas|Condimentos|Lacteos] = []

products_condimentos:List[Bebidas|Condimentos|Lacteos] = []

products_lacteos:List[Bebidas|Condimentos|Lacteos] = []


def read_data():
    """
        0 IdProducto
        1 NombreProducto
        2 Proveedor
        3 Categoria
        4 CantidadPorUnidad
        5 PrecioUnidad
        6 UnidadesEnExistencia
    """

    file = open('./data/Catalogo.csv', 'r', encoding="utf-8")

    # Not use columns name
    file.readline().replace("\n", "").split(",")

    products_lines = file.readlines()

    file.close()

    # Get the total countries in a list and sort them by their name
    for product_line in products_lines:
        product_list = product_line.replace("\n", "").split(",")

        idProducto = product_list[0]
        nombreProducto = product_list[1]
        proveedor = product_list[2]
        categoria = product_list[3]
        cantidadPorUnidad = product_list[4]
        precioUnidad = product_list[5]
        unidadesEnExistencia = product_list[6]

        price_formated = precioUnidad.replace("USD", "") 

        if categoria == "Bebidas":
            products_bebidas.append(Bebidas(
                int(idProducto),
                float(price_formated),
                int(unidadesEnExistencia),
                cantidadPorUnidad,
                proveedor,
            ))

        elif categoria == "Condimentos":
            products_condimentos.append(Condimentos(
                int(idProducto),
                float(price_formated),
                int(unidadesEnExistencia),
                cantidadPorUnidad,
                proveedor,
            ))

        elif categoria == "Lácteos":
            products_lacteos.append(Lacteos(
                int(idProducto),
                float(price_formated),
                int(unidadesEnExistencia),
                cantidadPorUnidad,
                proveedor,
            ))


def get_product_id_and_category(product_id):
    for product in products_bebidas:
        if product_id == product.get_id():
            return product, "bebidas"


    for product in products_condimentos:
        if product_id == product.get_id():
            return product, "condimentos"
        

    for product in products_lacteos:
        if product_id == product.get_id():
            return product, "lacteos"

    return None, None
