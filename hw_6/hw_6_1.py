import time

class TrafficLight:

    __color = 0

    def running(self):
        if self.__color == 0:
            print('TrafficLight is red')
            time.sleep(7)
            print('TrafficLight is yellow')
            time.sleep(2)
            print('TrafficLight is green')
            time.sleep(5)
        else:
            print('Error')

a = TrafficLight()
a.running()