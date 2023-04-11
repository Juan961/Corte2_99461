class Person():
    """
        A class used to represent a Persom

        ...

        Attributes
        ----------
        name : str
            the name of the person
        last_name : str
            the last name of the person
        age : int
            age of the person
        heigth : float
            heigth of the person
        weigth : float
            weigth of the person 

        Methods
        -------
        says(sound=None)
            Prints the animals name and what sound it makes
    """

    def __init__(self, name:str, last_name:str, age:int, height:float, weigth:float) -> None:
        self.__name = name
        self.__last_name= last_name
        self.__age = age
        self.__heigth = height
        self.__weigth = weigth

    # =================== Getters ===================

    def get_name(self): return self.__name

    def get_weigth(self): return self.__weigth

    def get_heigth(self): return self.__heigth

    # =================== Setters ===================

    def set_name(self, name:str):
        self.__name = name

    def set_heigth(self, heigth:float):
        if heigth < 40: raise Exception("Height not valid")

        self.__heigth = heigth

    def set_weigth(self, weigth:float):
        self.__weigth = weigth

    # =================== Methods ===================

    def __repr__(self) -> str:
        return f"{ self.__name } - { self.__last_name } - { self.__age }"

    def get_imc(self) -> str:
        imc = ( self.__weigth ) / ( ( self.__heigth / 100 ) ** 2 )

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
