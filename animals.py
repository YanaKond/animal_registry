# Родительский класс Животное
class Animal:
    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def age(self):
        from datetime import datetime
        today = datetime.today()
        birth_date = datetime.strptime(self.__birth_date, "%Y-%m-%d")
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def animal_info(self):
        return f"Имя: {self.get_name()}, Дата рождения: {self.get_birth_date()}, Возраст: {self.age()} лет"


# Класс ДомашниеЖивотные наследует от Животное
class DomesticAnimals(Animal):
    def __init__(self, name, birth_date, commands=None):
        super().__init__(name, birth_date)
        self.__commands = commands if commands else []

    def get_commands(self):
        return self.__commands

    def set_commands(self, commands):
        self.__commands = commands

    def add_command(self, command):
        self.__commands.append(command)

    def animal_info(self):
        commands = ', '.join(self.__commands) if self.__commands else "Команды отсутствуют"
        return f"Имя: {self.get_name()}, Дата рождения: {self.get_birth_date()}, Возраст: {self.age()} лет, Команды: {commands}"


# Класс Собака, наследуется от ДомашниеЖивотные
class Dog(DomesticAnimals):
    def __init__(self, name, birth_date, commands=None):
        super().__init__(name, birth_date, commands)


class Cat(DomesticAnimals):
    def __init__(self, name, birth_date, commands=None):
        super().__init__(name, birth_date, commands)


class Hamster(DomesticAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


# Класс ВьючныеЖивотные наследует от Животное
class WorkingAnimals(Animal):
    def __init__(self, name, birth_date, animal_type):
        super().__init__(name, birth_date)
        self.__animal_type = animal_type

    def get_animal_type(self):
        return self.__animal_type

    def animal_info(self):
        return f"Имя: {self.get_name()}, Дата рождения: {self.get_birth_date()}, Возраст: {self.age()} лет, Тип: {self.__animal_type}"


# Класс Лошадь наследуется от ВьючныеЖивотные
class Horse(WorkingAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date, "вьючное")


class Camel(WorkingAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date, "вьючное")


class Donkey(WorkingAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date, "вьючное")


# Пример использования
собака = Dog("Шарик", "2020-03-05", ["сидеть", "лежать"])
print(собака.animal_info())

кошка = Cat("Барсик", "2019-07-15", ["мяукать", "играть"])
print(кошка.animal_info())

хомяк = Hamster("Хомка", "2021-08-01")
print(хомяк.animal_info())

лошадь = Horse("Плотва", "2019-07-20")
print(лошадь.animal_info())

верблюд = Camel("Ваня", "2018-06-10")
print(верблюд.animal_info())

осел = Donkey("Иа", "2020-05-12")
print(осел.animal_info())

