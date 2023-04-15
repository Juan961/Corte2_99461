class Deportista:
    def __init__(self, name:str, document:int, age:int) -> None:
        self.set_name(name)
        self.set_document(document)
        self.set_age(age)

    def get_name(self): return self.__name
    def get_document(self): return self.__document
    def get_age(self): return self.__age

    def set_name(self, name:str):
        self.__name = name

    def set_document(self, document:int):
        self.__document = document

    def set_age(self, age:int):
        self.__age = age


    def medalla(self):
        print("Ha ganado una medalla")


class Tenis(Deportista):
    def __init__(self, name:str, document:int, age:int, sets_ganados:int, sets_perdidos:int) -> None:
        super().__init__(name, document, age)

        self.set_sets_ganados(sets_ganados)
        self.set_sets_perdidos(sets_perdidos)

    def get_sets_ganados(self): return self.__sets_ganados
    def get_sets_perdidos(self): return self.__sets_perdidos

    def set_sets_ganados(self, sets_ganados:int):
        self.__sets_ganados = sets_ganados

    def set_sets_perdidos(self, sets_perdidos:int):
        self.__sets_perdidos = sets_perdidos


    def medalla(self):
        print("Ha ganado una medalla en tenis")


class Basket(Deportista):
    def __init__(self, name:str, document:int, age:int, nombre_del_equipo:str, numero_cestas:int) -> None:
        super().__init__(name, document, age)

        self.set_nombre_del_equipo(nombre_del_equipo)
        self.set_numero_cestas(numero_cestas)

    def get_nombre_del_equipo(self): return self.__nombre_del_equipo
    def get_numero_cestas(self): return self.__numero_cestas

    def set_nombre_del_equipo(self, nombre_del_equipo:str):
        self.__nombre_del_equipo = nombre_del_equipo

    def set_numero_cestas(self, numero_cestas:int):
        self.__numero_cestas = numero_cestas


    def medalla(self):
        print("Ha ganado una medalla en basket")


class Futbol(Deportista):
    def __init__(self, name:str, document:int, age:int, nombre_del_equipo:str, numero_goles:int) -> None:
        super().__init__(name, document, age)

        self.set_nombre_del_equipo(nombre_del_equipo)
        self.set_numero_goles(numero_goles)

    def get_nombre_del_equipo(self): return self.__nombre_del_equipo
    def get_numero_cestas(self): return self.__numero_goles

    def set_nombre_del_equipo(self, nombre_del_equipo:str):
        self.__nombre_del_equipo = nombre_del_equipo

    def set_numero_goles(self, numero_goles:int):
        self.__numero_goles = numero_goles

    def medalla(self):
        print("Ha ganado una medalla en futbol")
