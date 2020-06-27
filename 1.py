# import itertools
import time
#
# class TrafficLight:
#
#     def colors(self):
#         all_colors = ['Red', 'Yellow', 'Green']
#         for color in cycle(all_colors):
#             if color == 'Red':
#                 time.sleep(7)
#             elif color == 'Yellow':
#                 time.sleep(2)
#             else:
#                 time.sleep(10)
#         return all_colors
#
#
# my_traffic = TrafficLight()

class TrafficLight:

    def color_red(self):
        print('Red')

    def color_yellow(self):
        print('Yellow')

    def color_green(self):
        print('Green')

my_colors = TrafficLight()
my_colors.color_red(), time.sleep(7)
my_colors.color_yellow(), time.sleep(2)
my_colors.color_green(), time.sleep(10)

