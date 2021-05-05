class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Поехала машина {self.name}."

    def stop(self):
        return f"Остановилась машина {self.name}."

    def turn(self):
        return f"Повернула машина {self.name}."

    def show_speed(self):
        return f"Скорость машины {self.speed} км/ч."


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Вы превысили скорость. Ваша скорость должна быть, {self.speed} км/ч."
        else:
            return f"Скорость {self.name} в норме"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Вы превысили скорость. Ваша скорость должна быть, {self.speed} км/ч."
        else:
            return f"Скорость {self.name} в норме"


class PoliceCar(Car):
    pass


town = TownCar(80, 'White', 'Audi', False)
print(town.go(), town.stop(), town.turn(), town.show_speed())
sport = SportCar(120, 'Yellow', 'Porsche', False)
print(sport.go(), sport.stop(), sport.turn(), sport.show_speed())
work = WorkCar(60, 'Black', 'Kia', False)
print(work.go(), work.stop(), work.turn(), work.show_speed())
police = PoliceCar(100, 'White', 'Ford', True)
print(police.go(), police.stop(), police.turn(), police.show_speed())
