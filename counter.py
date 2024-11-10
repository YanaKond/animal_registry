# Класс Счетчик
class Counter:
    def __init__(self):
        self.__count = 0
        self.__is_open = False

    def add(self):
        if not self.__is_open:
            raise Exception("Ресурс не открыт. Работа с объектом должна происходить в блоке try-with-resources.")
        self.__count += 1

    def get_count(self):
        return self.__count

    # Контекстный менеджер
    def __enter__(self):
        self.__is_open = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__is_open = False
        # Если произошла ошибка, бросаем исключение
        if exc_type is not None:
            raise Exception(f"Ошибка при работе с ресурсом: {exc_value}")

# Пример работы с Счетчиком и создания нового животного
class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def __str__(self):
        return f"Имя: {self.name}, Дата рождения: {self.birth_date}"

# Пример создания нового животного с использованием счетчика
def add_new_animal(counter, name, birth_date):
    if name and birth_date:  # Если все поля заполнены
        with counter:  # Используем счетчик в try-with-resources
            counter.add()
            new_animal = Animal(name, birth_date)
            print(f"Заведен новый питомец: {new_animal}")
    else:
        print("Ошибка: Заполнены не все поля животного.")

# Пример использования
counter = Counter()

# Завести несколько животных
add_new_animal(counter, "Шарик", "2020-03-05")
add_new_animal(counter, "Барсик", "2019-07-15")

# Проверка, сколько животных было заведено
print(f"Количество заведенных животных: {counter.get_count()}")

# Попытка использования счетчика вне блока try-with-resources (ошибка)
try:
    counter.add()
except Exception as e:
    print(f"Ошибка: {e}")

