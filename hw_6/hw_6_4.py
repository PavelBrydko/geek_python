class Car:

    speed = 0
    name = ''
    is_police = True

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, side):
        print(f'Машина повернула - {side}')

    def show_speed(self):
        return print(Car.speed)

class TownCar(Car):
    Car.show_speed = 100
    if Car.show_speed > 60:
        print('Скорость превышена')

class SportCar(Car):
    pass

class WorkCar(Car):
    if Car.show_speed > 60:
        print('Скорость превышена')

class PoliceCar(Car):
    Car.show_speed = 100

a = TownCar()
print(a.show_speed)
