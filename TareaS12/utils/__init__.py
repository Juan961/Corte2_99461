def format_file(columns, lines):
    foods = []

    for line in lines:
        new_line = line.replace("\n", "")

        food_list = new_line.split(",")

        food = {}

        food[columns[0]] = int(food_list[0])
        food[columns[1]] = food_list[1]
        food[columns[2]] = float(food_list[2])

        foods.append(food)

    return foods

def find_product_by_name(products, name):
    for product in products:
        if product.get("DESCRIPCION").lower() == name.lower():
            return product 

    return None
