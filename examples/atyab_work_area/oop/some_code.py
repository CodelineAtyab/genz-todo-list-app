from abc import ABC, abstractmethod

class Clock(ABC):
    _m = 50

    @abstractmethod
    def set_time(self, incoming_hour, incoming_min, incoming_sec):
        pass

    def get_time(self):
        return self.h, self.m, self.s


class AnalogClock(Clock):
    def __init__(self):
        self.__h = 0
        self.__m = 0
        self.__s = 0
        self.a = 10

    def set_time(self, incoming_hour, incoming_min, incoming_sec):
        print("In Analog Clock set time")

    def set_m(self, val):
        self.m = val
        if self.m > 59:
            self.__set_h(h+1)

    def display_time(self):
        return self.__h, self.__m, self.__s

    def __reset_hms(self):
        pass

    def __set_h(self, val):
        self.h = val

    def __set_s(self, val):
        self.s = val


analog_clock_instance = AnalogClock()
print(analog_clock_instance._m)


class User:
    email = "asdsadas@asdasd.com"

class ContactBook:
    def __init__(self, user):
        self.belongs_to = user


ContactBook(User())


