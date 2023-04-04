from models import Person

def main():
    person_1 = Person("Juan", "Garcia", 25, 170, 55)
    person_2 = Person("Pedro", "Garcia", 25, 188, 97)
    person_3 = Person("Maria", "Garcia", 25, 160, 47)
    person_4 = Person("Julian", "Garcia", 25, 158, 58)
    person_5 = Person("Jessica", "Garcia", 25, 170, 73)

    print(person_1.get_imc())
    print(person_2.get_imc())
    print(person_3.get_imc())
    print(person_4.get_imc())
    print(person_5.get_imc())

if __name__ == "__main__":
    main()
