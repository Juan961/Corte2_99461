class Citizen:
    def __init__(self, name:str, id:int, age:int) -> None:
        self.__name = name
        self.__id = id
        self.__age = age

    def say_hi(self) -> str:
        return f"Hi my name is {self.__name}"


class Writer(Citizen):
    def __init__(self, name:str, id:int, age:int, latest_book:str, latest_award:str) -> None:
        super().__init__(name, id, age)
        self.__latest_book = latest_book
        self.__latest_award = latest_award

    def write(self) -> str:
        return "I'm writing, shut up"


class Secretary(Citizen):
    def __init__(self, name:str, id:int, age:int, boss: Citizen, boss_schedule_is_organized:bool) -> None:
        super().__init__(name, id, age)
        self.__boss = boss
        self.__boss_schedule_is_organized = boss_schedule_is_organized

    def organize_schedule(self) -> None:
        if not self.__boss_schedule_is_organized:
            self.__boss_schedule_is_organized = True

    def get_boss_schedule_is_organized(self) -> str:
        return str(self.__boss_schedule_is_organized)


class Physicist(Citizen):
    def __init__(self, name:str, id:int, age:int, latest_discovery:str, university:str) -> None:
        super().__init__(name, id, age)
        self.__latest_discovery = latest_discovery
        self.__university = university

    def research(self) -> str:
        return "Research findings: .."

    def say_hi(self) -> str:
        return "Nobody exists on purpose. Nobody belongs anywhere. Everybody's gonna die"
