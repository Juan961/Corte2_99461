class Person():
    def __init__(self, name:str, last_name:str, age:int, height:float, weigth:float) -> None:
        self.name = name
        self.last_name= last_name
        self.age = age
        self.height = height
        self.weigth = weigth

    def __repr__(self) -> str:
        return f"{ self.name } - { self.last_name } - { self.age }"

    def speak(self):
        print(f"Hola mi nombre es { self.name }")

    def get_imc(self) -> str:
        imc = ( self.weigth ) / ( ( self.height / 100 ) ** 2 )

        if imc <= 18.5:
            return "Por debajo"
        elif 18.5 < imc <= 24.9:
            return "Saludable"
        elif 25 < imc <= 29.9:
            return "Sobrepeso"
        elif 30 < imc <= 34.9:
            return "Obesidad I"
        elif 35 < imc <= 39.9:
            return "Obesidad II"
        else:
            return "Obesidad III"

    @staticmethod
    def hi():
        print(f"Hola")

class Student(Person):
    def __init__(self):
        super()
