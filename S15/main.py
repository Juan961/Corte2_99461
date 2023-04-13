from models import Deportista, Tenis, Basket, Futbol

def main():
    fal = Deportista("Falcao", 123123214, 36)
    fal_2 = Futbol("Falcao 2", 123123214, 36, "Selección", 20)

    fal.medalla()
    fal_2.medalla()

    tenis = Tenis("Teni", 123123214, 36, 20, 20)
    bask = Basket("Bas", 123123214, 36, "Na", 20)


if __name__ == "__main__":
    main()
