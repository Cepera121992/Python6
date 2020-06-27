class Car:
    def go(self):
        car_speed = int(input('Текущая скорость автомобиля: '))
        car_color = input('Напишите цвет автомобиля: ')
        car_name = input('Напишите марку автомобиля: ')
        car_is_police = bool(input('Это полицейская машина? True/False: '))
        print('Машина поехала')

    def stop(self):
        car_speed = int(input('Текущая скорость автомобиля: '))
        car_color = input('Напишите цвет автомобиля: ')
        car_name = input('Напишите марку автомобиля: ')
        car_is_police = bool(input('Это полицейская машина? True/False: '))
        print('Машина остановилась')

    def turn(self):
        car_speed = int(input('Текущая скорость автомобиля: '))
        car_color = input('Напишите цвет автомобиля: ')
        car_name = input('Напишите марку автомобиля: ')
        car_is_police = bool(input('Это полицейская машина? True/False: '))
        turning_dir = input('Введите направление поворота: ')
        if turning_dir == 'налево' or turning_dir == 'Налево':
            print('Машина повернула налево')
        else:
            print('Машина повернула направо')

    def show_speed(self):
        car_speed = int(input('Текущая скорость автомобиля: '))
        car_color = input('Напишите цвет автомобиля: ')
        car_name = input('Напишите марку автомобиля: ')
        car_is_police = bool(input('Это полицейская машина? True/False: '))
        return car_speed


class TownCar(Car):
    def show_speed(self):
        car_speed = int(input('Текущая скорость автомобиля: '))
        if car_speed > 60:
            print('Скорость превышена!')
        else:
            pass

class SportCar(Car):
    def show_speed(self):
        car_speed = int(input('Текущая скорость автомобиля: '))
        if car_speed > 80:
            print('Скорость превышена!')
        else:
            pass


class WorkCar(Car):
    def show_speed(self):
        car_speed = int(input('Текущая скорость автомобиля: '))
        if car_speed > 40:
            print('Скорость превышена!')
        else:
            pass


class Police(Car):
    def show_speed(self):
        car_speed = int(input('Текущая скорость автомобиля: '))
        if car_speed > 80:
            print('Ничего страшного! Ты же полиция.')
        else:
            pass

my_car = TownCar
my_car.show_speed(70)