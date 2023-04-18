from models import Citizen, Colombia, Inglaterra, China, dar_saludo


def main():
    col = Colombia("Español", "Juan", 12315125215)
    ing = Inglaterra("Inglés", "Juan", 12315125215)
    chin = China("Mandarín", "Juan", 12315125215)
    ciu = Citizen("Frances", "Carla")

    print( dar_saludo(col) )
    print( dar_saludo(ing) )
    print( dar_saludo(chin) )
    print( dar_saludo(ciu) )


if __name__ == "__main__":
    main()
