import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        while True:
            self.__color = "Красный"
            print(self.__color)
            time.sleep(7)

            self.__color = "Желтый"
            print(self.__color)
            time.sleep(2)

            self.__color = "Зеленый"
            print(self.__color)
            time.sleep(5)


light_signal = TrafficLight()
print(light_signal.running())
