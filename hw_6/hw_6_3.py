class Worker:

    name = ''
    surname = ''
    position = ''
    _income = {
        "wage": 10000,
        "bonus": 15000
    }

class Position(Worker):

    def get_full_name(self):
        pass

    def get_total_income(self):
        total_income = sum(_income.values())
        return total_income

a = Position()
print(a.get_total_income)
