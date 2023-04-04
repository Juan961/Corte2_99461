from utils import format_file , find_product_by_name

def main():
    try:
        file = open("alimentos.txt", "r")

        columns = file.readline()
        columns = columns.replace("\n", "").split(",")

        lines = file.readlines()

        file.close()

        foods = format_file(columns, lines)

        continue_search = True

        while continue_search:
            try:
                item = int(input("1. Find product\n2. Exit\nOption: "))

                if item == 1:
                    product_category = input("Insert the product name: ")

                    product = find_product_by_name(foods, product_category)

                    if not product:
                        print("Product not found")
                        continue
        
                    IVA = product.get("TARIFA IVA LEY VIGENTE")

                    product_value = float(input("Enter the product value: "))

                    product_value_without_IVA = round(product_value - ( product_value * IVA ) , 2)
                    iva_value = round(product_value * IVA, 2)

                    print(f"Product value without IVA: { product_value_without_IVA }")
                    print(f"IVA value: { iva_value }")
                
                elif item == 2:
                    continue_search = False
            except ValueError:
                print("Invalid option")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
