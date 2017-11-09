class Time:
    """time of day"""


def print_time(t1):
    return '{}:{}:{}'.format(t1.hour, t1.minute, t1.second)


def is_after(t1, t2):
    t1_seconds = (t1.hour * 3600) + (t1.minute * 60) + t1.second
    t2_seconds = (t2.hour * 3600) + (t2.minute * 60) + t2.second
    return t1_seconds < t2_seconds


class Time2:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        if isinstance(other, Time2):
            seconds = self.add_time(other)
        else:
            seconds = self.increment(other)
        return seconds

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return '{}:{}:{}'.format(self.hour, self.minute, self.second)

    def __sub__(self, other):
        seconds = self.time_to_int() - other.time_to_int()
        return int_to_time(seconds)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return seconds

    def print_time2(self):
        print('{}:{}:{}'.format(self.hour, self.minute, self.second))

    def time_to_int(self):
        result = (self.hour * 3600) + (self.minute * 60) + self.second
        return result

    def increment(self, seconds):
        seconds = seconds + self.time_to_int()
        return int_to_time(seconds)


def int_to_time(x):
    hours = int(x/3600)
    minutes = int((x-(hours*3600))/60)
    seconds = int(x-(hours*3600)-(minutes*60))
    return '{}:{}:{}'.format(hours, minutes, seconds)


def main():
    t1, t2, t3 = Time2(), Time2(), Time2()
    t1.hour, t1.minute, t1.second = 0, 12, 1
    t2.hour, t2.minute, t2.second = 0, 50, 2
    t4 = Time2(20, 59, 00)

    # t1.print_time2()
    # t2.print_time2()
    #
    # t1.time_to_int()
    # t2.time_to_int()
    # t3.print_time2()
    t4.print_time2()
    print('t4+10=', t4.increment(110))

    start = Time2(11, 45, 0)
    duration = Time2(1, 10, 10)
    end = start + duration
    print('{} + {} = {}'.format(start, duration, end))

    end = Time2(12, 55, 10)
    duration = end - start
    print('{} - {} = {}'.format(end, start, duration))

    duration_int = 600
    end = start + duration_int
    print('{} + {} = {}'.format(start, duration_int, end))

    duration_int = 3600
    end = duration_int + start
    print('{} + {} = {}'.format(duration_int, start, end))

    # print(is_after(t1, t2))


if __name__ == '__main__':
    main()
