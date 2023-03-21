import ast

mi_lista = [2, 4, 6, 2]

option = ""

while option != "exit":
    option = input("Option: ")

    if option == "append":
        value = int(input("Insert the value to add: "))
        mi_lista.append(value)

    elif option == "pop":
        index = int(input("Insert index of the value to delete: "))
        mi_lista.pop(index)

    elif option == "sum":
        print(f"Suma: { sum( mi_lista ) }")

    elif option == "count":
        value = int(input("Value to count: "))
        print(f"Count: { mi_lista.count(value) }")

    elif option == "in":
        value = int(input("Insert value to check: "))
        print(f"El valor existe { value in mi_lista }")

    elif option == "extend":
        index = input("Insert the list [2, 3]: ")
        mi_lista.extend(ast.literal_eval(index))

    print(mi_lista)
