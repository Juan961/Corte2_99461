class Citizen():
    def __init__(self, idioma:str, nombre:str) -> None:
        self.__nombre = nombre
        self.__idioma = idioma


    def get_nombre(self): return self.__nombre

    def get_idioma(self): return self.__idioma


    def set_nombre(self, nombre:str):
        self.__nombre = nombre

    def set_idioma(self, idioma:str):
        self.__idioma = idioma

    def saludo(self):
        return "Quoi de Bebau!"


class Colombia(Citizen):
    def __init__(self, idioma:str, nombre:str, cc:int) -> None:
        super().__init__(idioma, nombre)
        self.__cc = cc

    def get_cc(self):
        return self.__cc

    def set_cc(self, cc):
        self.__cc = cc
    
    def saludo(self):
        return "Qiubo parce"


class Inglaterra(Citizen):
    def __init__(self, idioma:str, nombre:str, id:int) -> None:
        super().__init__(idioma, nombre)
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def saludo(self):
        return "Morning"


class China(Citizen):
    def __init__(self, idioma:str, nombre:str, shengfenzheng:int) -> None:
        super().__init__(idioma, nombre)
        self.__shengfenzheng = shengfenzheng

    def get_shengfenzheng(self):
        return self.__shengfenzheng

    def set_shengfenzheng(self, shengfenzheng):
        self.__shengfenzheng = shengfenzheng

    def saludo(self):
        return "NiGanMaya!!"

def dar_saludo(obj:Citizen) -> str:
    return obj.saludo()
