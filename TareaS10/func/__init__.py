from typing import List

import random

from utils import is_prime

def random_function():
    try:
        random_list = []

        for _ in range(10):
            random_list.append(random.randint(1, 50))

        print(f"List generated: { random_list }")

        def custom_max(_list:List[int]):
            _list.sort(reverse=True)
            print(f"Max: { _list[0] }")

        def custom_min(_list:List[int]):
            _list.sort()
            print(f"Min: { _list[0] } ")
        
        def find_primes(_list:List[int]):
            prime_list = []

            for i in _list:
                if is_prime(i):
                    prime_list.append(i)

            print(f"Prime list: { prime_list }")

        custom_max(random_list.copy())
        custom_min(random_list.copy())
        find_primes(random_list.copy())

    except Exception as e:
        print(e)

def schedule():
    """
        Consultar su horario de clases
        Ingresando el nombre de la materia indique el día de clase, la hora, el salón y el nombre del profesor.
        Index of each property
            0. Name
            1. Day
            2. Hour
            3. Classroom
            4. Professor
    """

    try:
        schedule_list:List[List[str]] = [
            [ "Cálculo integral", "Martes, Jueves", "7:00 - 9:00", "406 DB", "Jairo Lalinde" ],
            [ "Física mecánica", "Martes, Jueves", "9:00 - 11:00", "404 DB", "Roberto Bohórquez" ],
            [ "Programación", "Martes, Jueves", "13:00 - 15:00", "30? GO", "David Torres" ],
            [ "Constitución", "Miércoles", "7:00 - 9:00", "405 DB", "Yuberney" ],
            [ "Circuitos DC", "Miércoles, Viernes", "11:00 - 13:00", "306 DB", "Roberto Bohórquez" ],
            [ "Cultura ecológica", "Viernes", "9:00 - 11:00", "306 PS", "Yuberney" ],
            [ "Taller de física mecánica", "Viernes", "15:00 - 17:00", "406 DB", "Paula" ]
        ]

        option = input("Insert the name of the the course: ")

        for schedule in schedule_list:

            if schedule[0].lower() == option.lower():
                print(f"Name: { schedule[0] }")
                print(f"Day(s): { schedule[1] }")
                print(f"Hour: { schedule[2] }")
                print(f"Classroom: { schedule[3] }")
                print(f"Professor: { schedule[4] }")

                return

        print("The course doesn't exist. Check tildes. The filter is not case sensitive")
        print(f"The list of courses is")

        for schedule in schedule_list:
            print(f"\t - { schedule[0] }")

    except Exception as e:
        print(e)
