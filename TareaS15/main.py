from models import Writer, Secretary, Physicist

def main():
    try:
        mario = Writer("Mario Mendoza", 9898989494, 59, "Leer es resistir", "Premio Biblioteca Breve")

        miguel = Secretary("Miguel", 9841232112, 59, mario, False)

        idk = Physicist("Idk", 4783274832, 123, "Neutron stars", "Universidad Nacional")

        print("========================= Writer =========================")
        print(mario.write())

        print("========================= Secretary =========================")
        miguel.organize_schedule()
        print(f"Boss schedule is organized: {miguel.get_boss_schedule_is_organized()}")

        print("========================= Physicist =========================")
        print(idk.research())
        print(idk.say_hi())

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
