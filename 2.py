# Два решения

# class Road:
#     def _my_data(self, numbers):
#         lenght, width, mass, depth = (numbers)
#         my_road = lenght * width * mass * depth
#         return my_road
# my_numbers = Road()
# print(my_numbers._my_data((1, 2, 3, 4)))


class Road:
    def _lenght(self):
        lenght_num = int(input('Введите длину дороги: '))
        return lenght_num
    def _width(self):
        width_num = int(input('Введите ширину дороги: '))
        return width_num
    def _depth(self):
        depth_num = int(input('Введите толщину асфальта: '))
        return depth_num
    def _mass(self):
        mass_num = int(input('Введите массу асфальта: '))
        return mass_num

data = Road()
my_data = data._lenght() * data._width() * data._mass() * data._depth()
print(my_data)