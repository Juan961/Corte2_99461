# Estudiantes
# - Juan Jose Garcia Pinzon
# - Andrés Felipe Benavides Cabrera

from data import read_data
from data import get_product_id_and_category


cart_bebidas = { "cantidad": 0, "precioTotal": 0.0 }
cart_condimentos = { "cantidad": 0, "precioTotal": 0.0 }
cart_lacteos = { "cantidad": 0, "precioTotal": 0.0 }


def imprimir():
    print("=================== Total ===================")

    print("Bebidas: ")
    print(f"Cantidad: { cart_bebidas['cantidad'] }")
    print(f"Precio acumulado: { cart_bebidas['precioTotal'] } \n")

    print("Condimentos: ")
    print(f"Cantidad: { cart_condimentos['cantidad'] }")
    print(f"Precio acumulado: { cart_condimentos['precioTotal'] } \n")

    print("Lacteos: ")
    print(f"Cantidad: { cart_lacteos['cantidad'] }")
    print(f"Precio acumulado: { cart_lacteos['precioTotal'] } \n")

    print(f"Valor total: { cart_bebidas['precioTotal'] + cart_condimentos['precioTotal'] + cart_lacteos['precioTotal'] }")


def facturar():
    product_id = input("Ingrese el id del articulo para facturar. De lo contrario 'fin': ")

    if product_id == "fin":
        print("")
        imprimir()
        return False

    product_id = int(product_id)

    product, categoria = get_product_id_and_category(product_id)

    if not product: raise Exception("Product not found")

    if categoria == "bebidas":
        unidades = product.get_unid_existencia()

        if unidades == 0:
            print("Existencia insuficiente\n")
            return True

        product.set_unid_existencia( product.get_unid_existencia() - 1 )

        cart_bebidas["cantidad"] += 1
        cart_bebidas["precioTotal"] = cart_bebidas["precioTotal"] + ( 1 * product.get_precio_base() )


    elif categoria == "condimentos":
        unidades = product.get_unid_existencia()

        if unidades == 0:
            print("Existencia insuficiente\n")
            return True

        product.set_unid_existencia( product.get_unid_existencia() - 1 )

        cart_condimentos["cantidad"] += 1
        cart_condimentos["precioTotal"] = cart_condimentos["precioTotal"] + ( 1 * product.get_precio_base() )

    elif categoria == "lacteos":
        unidades = product.get_unid_existencia()

        if unidades == 0:
            print("Existencia insuficiente\n")
            return True

        product.set_unid_existencia( product.get_unid_existencia() - 1 )

        cart_lacteos["cantidad"] += 1
        cart_lacteos["precioTotal"] = cart_lacteos["precioTotal"] + ( 1 * product.get_precio_base() )

    print(f"Artículo añadido\n")

    return True


def main():
    try:
        read_data()

        continue_menu = True

        while continue_menu:
            continue_menu = facturar()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
