# Abstraction
# Основные атрибуты объектаб относящиеся ко всем объектам класса

# Наследование
# Процесс перенятия методов и объектов родительского класса в дочерний
# Даймонд проблем решается в ширину
# Остальное в глубину


# Example:
class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower
        self.speed = 0

    def drive(self):
        print("driving")


class ElectricCar(Car):
    def __init__(self, model, horsepower, battery_size):
        super().__init__(model, horsepower)
        self.battery_size = battery_size

    def charge(self):
        print("charging")


# При наследовании от нескольких классов одновременно родитель с конструктором(__init__) должен идти последним


# Encapsulation
# @property - когда хочешь посмотреть значение атрибута
# @name.setter - когда хочешь изменить значение атрибута или провести некоторые действия

# Polymorphism(переопределение родительских частей внутри дочерних, не меняя родительский класс) - used only for add functionality parent class, and !NEVER! change parent class and it's attributes
# Так же для запрета использования родительских атрибутов в дочерних, with use of "raise exception"  in method
# super().__init__(model, horsepower) - при наследовании передает родительские атрибуты в родительский класс
