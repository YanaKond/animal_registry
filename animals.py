# Родительский класс Животное
class Животное:
    def __init__(self, имя, дата_рождения):
        self.__имя = имя
        self.__дата_рождения = дата_рождения

    def get_имя(self):
        return self.__имя

    def get_дата_рождения(self):
        return self.__дата_рождения

    def возраст(self):
        from datetime import datetime
        today = datetime.today()
        birth_date = datetime.strptime(self.__дата_рождения, "%Y-%m-%d")
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def животное_информация(self):
        return f"Имя: {self.get_имя()}, Дата рождения: {self.get_дата_рождения()}, Возраст: {self.возраст()} лет"


# Класс ДомашниеЖивотные наследует от Животное
class ДомашниеЖивотные(Животное):
    def __init__(self, имя, дата_рождения, команды=None):
        super().__init__(имя, дата_рождения)
        self.__команды = команды if команды else []

    def get_команды(self):
        return self.__команды

    def set_команды(self, команды):
        self.__команды = команды

    def добавить_команду(self, команда):
        self.__команды.append(команда)

    def животное_информация(self):
        команды = ', '.join(self.__команды) if self.__команды else "Команды отсутствуют"
        return f"Имя: {self.get_имя()}, Дата рождения: {self.get_дата_рождения()}, Возраст: {self.возраст()} лет, Команды: {команды}"


# Класс Собака, наследуется от ДомашниеЖивотные
class Собака(ДомашниеЖивотные):
    def __init__(self, имя, дата_рождения, команды=None):
        super().__init__(имя, дата_рождения, команды)


class Кошка(ДомашниеЖивотные):
    def __init__(self, имя, дата_рождения, команды=None):
        super().__init__(имя, дата_рождения, команды)


class Хомяк(ДомашниеЖивотные):
    def __init__(self, имя, дата_рождения):
        super().__init__(имя, дата_рождения)


# Класс ВьючныеЖивотные наследует от Животное
class ВьючныеЖивотные(Животное):
    def __init__(self, имя, дата_рождения, тип_животного):
        super().__init__(имя, дата_рождения)
        self.__тип_животного = тип_животного

    def get_тип_животного(self):
        return self.__тип_животного

    def животное_информация(self):
        return f"Имя: {self.get_имя()}, Дата рождения: {self.get_дата_рождения()}, Возраст: {self.возраст()} лет, Тип: {self.__тип_животного}"


# Класс Лошадь наследуется от ВьючныеЖивотные
class Лошадь(ВьючныеЖивотные):
    def __init__(self, имя, дата_рождения):
        super().__init__(имя, дата_рождения, "вьючное")


class Верблюд(ВьючныеЖивотные):
    def __init__(self, имя, дата_рождения):
        super().__init__(имя, дата_рождения, "вьючное")


class Осел(ВьючныеЖивотные):
    def __init__(self, имя, дата_рождения):
        super().__init__(имя, дата_рождения, "вьючное")


# Пример использования
собака = Собака("Шарик", "2020-03-05", ["сидеть", "лежать"])
print(собака.животное_информация())

кошка = Кошка("Барсик", "2019-07-15", ["мяукать", "играть"])
print(кошка.животное_информация())

хомяк = Хомяк("Хомка", "2021-08-01")
print(хомяк.животное_информация())

лошадь = Лошадь("Плотва", "2019-07-20")
print(лошадь.животное_информация())

верблюд = Верблюд("Ваня", "2018-06-10")
print(верблюд.животное_информация())

осел = Осел("Иа", "2020-05-12")
print(осел.животное_информация())

