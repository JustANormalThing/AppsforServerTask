class Car:
    def __init__(self,id,Марка,Модель,Год,Цвет,Цена,Регист):
        self.id = int(id)
        self.Марка = Марка
        self.Модель = Модель
        self.Год = int(Год)
        self.Цвет = Цвет
        self.Цена = float(Цена)
        self.Регист = Регист


cars = [
    Car("1", "Toyota", "Camry", 2018, "Red", 20000, "Flan"),
    Car("2", "Honda", "Civic", 2015, "Blue", 15000, "Reimu"),
    Car("3", "Toyota", "Corolla", 2020, "White", 18000000000, "Marais"),
    Car("4", "Ford", "Focus", 2012, "Black", 12000, "Reisa"),
    Car("5", "Honda", "Accord", 2017, "Gray", 22000, "Star"),
    Car("6", "Honda", "Accord", 2025, "Gray", 22000, "Sunny"),
    Car("7", "Honda1", "Accord1", 2025, "Gray", 22000, "Sunny"),
    Car("8", "Honda", "Accord2", 2024, "Gray", 22000, "Sunny")
]

def cars1(mark):
    return [car for car in cars if car.Марка == mark]

def cars2(model, n):
    current_year = 2025
    return [car for car in cars if car.Модель == model and (current_year - car.Год) > n]

def AAAAAA(year,b):
    return[car for car in cars if car.Год == year and car.Цена > b]

print("Автомобили марки Toyota:", [car.Модель for car in cars1("Toyota")])
print("Модели Honda:", [car.Модель for car in cars2("Civic", 10)])
print("Модель:",[car.Модель for car in AAAAAA(2025,21000)])

