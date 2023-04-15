class Citizen:

    @staticmethod
    def __repr__() -> str:
        return """ Model Citizen:
            - nombre:str
            - cedula:int
            - edad:int

            + set_nombre(nombre:str):None
            + set_cedula(cedula:int):None
            + set_edad(edad:int):None

            + get_nombre():str
            + get_cedula():int
            + get_edad():int

            + mostrar():str
            + es_mayor_de_edad():bool
        """.replace("\t", "")


def main():
    try:
        # https://pep8.org/#method-names-and-instance-variables
        print(Citizen.__repr__())

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
