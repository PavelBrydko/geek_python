class Stationery:

    title = ''

    def draw(self):
        print('“Запуск отрисовки.')


class Pen(Stationery):
    Stationery.draw = 'Отрисовка 1'

class Pencil(Stationery):
    Stationery.draw = 'Отрисовка 2'

class Handle(Stationery):
    Stationery.draw = 'Отрисовка 3'
