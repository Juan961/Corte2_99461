class Articulos:
    def __init__(self, id:int, precio_base:float, unid_existencia:int) -> None:
        self.__id = id
        self.__precio_base = precio_base
        self.__unid_existencia = unid_existencia

    def get_id(self):
        return self.__id

    def set_precio_base(self, precio_base:float):
        self.__precio_base = precio_base
    def set_unid_existencia(self, unid_existencia:int):
        self.__unid_existencia = unid_existencia

    def get_precio_base(self): return self.__precio_base
    def get_unid_existencia(self): return self.__unid_existencia

    def precio_final(self):
        pass


class Bebidas(Articulos):
    def __init__(self, id:int, precio_base:float, unid_existencia:int, cant_unidad:str, proveedor:str) -> None:
        super().__init__(id, precio_base, unid_existencia)

        self.__cant_unidad = cant_unidad
        self.__proveedor = proveedor

    def set_cant_unidad(self, cant_unidad:str):
        self.__cant_unidad = cant_unidad

    def set_proveedor(self, proveedor:str):
        self.__proveedor = proveedor

    def get_cant_unidad(self): return self.__cant_unidad
    def get_proveedor(self): return self.__proveedor

    def precio_final(self):
        pass


class Lacteos(Articulos):
    def __init__(self, id:int, precio_base:float, unid_existencia:int, cant_unidad:str, proveedor:str) -> None:
        super().__init__(id, precio_base, unid_existencia)

        self.__cant_unidad = cant_unidad
        self.__proveedor = proveedor

    def set_cant_unidad(self, cant_unidad:str):
        self.__cant_unidad = cant_unidad

    def set_proveedor(self, proveedor:str):
        self.__proveedor = proveedor

    def get_cant_unidad(self): return self.__cant_unidad
    def get_proveedor(self): return self.__proveedor

    def precio_final(self):
        pass


class Condimentos(Articulos):
    def __init__(self, id:int, precio_base:float, unid_existencia:int, cant_unidad:str, proveedor:str) -> None:
        super().__init__(id, precio_base, unid_existencia)

        self.__cant_unidad = cant_unidad
        self.__proveedor = proveedor

    def set_cant_unidad(self, cant_unidad:str):
        self.__cant_unidad = cant_unidad

    def set_proveedor(self, proveedor:str):
        self.__proveedor = proveedor

    def get_cant_unidad(self): return self.__cant_unidad
    def get_proveedor(self): return self.__proveedor

    def precio_final(self):
        pass
