import json
from datetime import datetime


# 1. Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Неизвестный звук"

    def eat(self):
        return f"{self.name} кушает"

    def __str__(self):
        return f"{self.name}, {self.age} лет"


# 2. Наследование - подклассы животных
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Специфический атрибут

    def make_sound(self):
        return "Чирик-чирик!"

    def fly(self):
        return f"{self.name} летает с размахом крыльев {self.wing_span}см"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Специфический атрибут

    def make_sound(self):
        return "Рррр!"

    def run(self):
        return f"{self.name} бегает"


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # Специфический атрибут

    def make_sound(self):
        return "Шшшш!"

    def crawl(self):
        return f"{self.name} ползает"


# 5. Классы для сотрудников
class ZooEmployee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} - {self.position}"


class ZooKeeper(ZooEmployee):
    def __init__(self, name):
        super().__init__(name, "Смотритель")

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}"


class Veterinarian(ZooEmployee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}"


# 4. Композиция - класс Zoo
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []  # Композиция - животные принадлежат зоопарку
        self.employees = []  # Композиция - сотрудники принадлежат зоопарку

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} принят на работу")

    def show_animals(self):
        print(f"\nЖивотные в зоопарке '{self.name}':")
        for animal in self.animals:
            print(f"  - {animal}")

    def show_employees(self):
        print(f"\nСотрудники зоопарка '{self.name}':")
        for employee in self.employees:
            print(f"  - {employee}")

    # Дополнительно: сохранение в файл
    def save_to_file(self, filename):
        data = {
            'zoo_name': self.name,
            'animals': [
                {
                    'type': type(animal).__name__,
                    'name': animal.name,
                    'age': animal.age
                } for animal in self.animals
            ],
            'employees': [
                {
                    'name': emp.name,
                    'position': emp.position
                } for emp in self.employees
            ],
            'saved_at': datetime.now().isoformat()
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"\nИнформация о зоопарке сохранена в файл {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.name = data['zoo_name']
            print(f"\nЗагружен зоопарк: {self.name}")

        except FileNotFoundError:
            print(f"Файл {filename} не найден")


# 3. Полиморфизм - функция для демонстрации
def animal_sound(animals):
    print("\nЗвуки животных (полиморфизм):")
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")


# Демонстрация работы
if __name__ == "__main__":
    # Создаем зоопарк
    my_zoo = Zoo("Рязанский зоопарк")

    # Создаем животных разных типов
    parrot = Bird("Кеша", 2, 30)
    lion = Mammal("Симба", 5, "золотистый")
    snake = Reptile("Каа", 3, "чешуйчатый")
    elephant = Mammal("Дамбо", 10, "серый")

    # Создаем сотрудников
    keeper = ZooKeeper("Иван Петров")
    vet = Veterinarian("Мария Сидорова")

    # Добавляем животных и сотрудников в зоопарк
    my_zoo.add_animal(parrot)
    my_zoo.add_animal(lion)
    my_zoo.add_animal(snake)
    my_zoo.add_animal(elephant)

    my_zoo.add_employee(keeper)
    my_zoo.add_employee(vet)

    # Показываем информацию
    my_zoo.show_animals()
    my_zoo.show_employees()

    # Демонстрируем полиморфизм
    animal_sound(my_zoo.animals)

    # Демонстрируем специфические методы животных
    print("\nСпецифические методы животных:")
    print(parrot.fly())
    print(lion.run())
    print(snake.crawl())

    # Демонстрируем методы сотрудников
    print("\nРабота сотрудников:")
    print(keeper.feed_animal(lion))
    print(vet.heal_animal(parrot))

    # Демонстрируем методы eat() (наследование)
    print("\nКормление животных:")
    for animal in my_zoo.animals:
        print(animal.eat())

    # Сохраняем информацию в файл
    my_zoo.save_to_file("zoo_data.json")

    # Загружаем информацию (демонстрация)
    new_zoo = Zoo("Новый зоопарк")
    new_zoo.load_from_file("zoo_data.json")