from models import Person

def main():
    yo = Person("Juan", "García", 19, 170.0, 70.0)

    print(yo.__repr__())
    print(yo.get_imc())

if __name__ == "__main__":
    main()
