class Worker:
    def name(self):
        print('name')
    def surname(self):
        print('surname')
    def position(self):
        print('position')
    def _income(self):
        income = {"wage": wage, "bonus": bonus}
        print('income')

class Position(Worker):
    def get_full_name(self):
        full_name = input('Введите полное имя сотрудника:')
        return full_name
    def get_total_income(self):
        wage = int(input('Введите зарплату: '))
        bonus = int(input('Введите премию: '))
        total_income = wage + bonus
        return total_income

human = Position()
# human.get_full_name()
print(human.get_total_income())
