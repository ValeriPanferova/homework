class Stationery:
    title = 'Запуск отрисовки'

    def draw(self):
        return self.title


class Pen(Stationery):
    title = 'Запускаю отрисовку ручкой'

    def draw(self):
        return self.title


class Pencil(Stationery):
    title = 'Запускаю отрисовку карандашом'

    def draw(self):
        return self.title


class Handle(Stationery):
    title = 'Запускаю отрисовку маркером'

    def draw(self):
        return self.title


st = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
print(st.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
