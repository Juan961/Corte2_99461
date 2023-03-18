import random
import math

from utils import custom_radians_to_degress, custom_degress_to_radians, is_pair

def random_function():
    try:
        digits = 0
        required = "pair"

        while digits < 10:
            number = random.randint(100, 120)

            if number == 110 or number == 115 or number == 119:
                continue

            elif required == "pair" and is_pair(number):
                digits += 1
                required = "notPair"
                print(number)

            elif required == "notPair" and not is_pair(number):
                digits += 1
                required = "pair"
                print(number)

    except Exception as e:
        print(e)

def calculate():
    try:
        operation = int(input("Ingrese la función\n1. Sen\n2. Cos\n3. Tan\n4. Exp\n5. Logaritmo natural\nOpción: "))
        number = float(input("Ingrese el número para calcular: "))

        if operation == 1 or operation == 2 or operation == 3:
            input_type = int(input("El número esta en\n1. Radianes\n2. Grados\nOpción: "))

            if input_type == 2:
                number_radians = custom_degress_to_radians(number)
            else:
                number_radians = number

        if operation == 1:
            result = round( math.sin(number_radians), 4 )
            print(f"El resultado de sin({ number }) es: { result }")

        elif operation == 2:
            result = round( math.cos(number_radians), 4 )
            print(f"El resultado de cos({ number }) es: { result }")

        elif operation == 3:
            result = round( math.tan(number_radians), 4 )
            print(f"El resultado de tan({ number }) es: { result }")

        elif operation == 4:
            result = round( math.exp(number), 4 )
            print(f"El resultado de exp({ number }) es { result }")

        elif operation == 5:
            result = round( math.log(number), 4 )
            print(f"El resultado de logn({ number }) es { result }")

        else:
            raise Exception("Out of range")

    except Exception as e:
        print(e)
