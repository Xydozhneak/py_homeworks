class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value
        self.set_max(max_value)
        self.set_min(min_value)
        self.set_current(current)

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError("Start value of counter isn`t include.")

    def set_max(self, max_max):
        if max_max >= self.min_value:
            self.max_value = max_max
        else:
            raise ValueError("Max value should be not less then min value.")

    def set_min(self, min_min):
        if min_min <= self.max_value:
            self.min_value = min_min
        else:
            raise ValueError("Min value should be more then Max value.")

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Limit max")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Limit min")

    def get_current(self):
        return self.current

    def __str__(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
print(counter.current)
counter.step_up()
print(counter.current)
counter.step_up()
print(counter.current)
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()
    print(counter.current)
except ValueError as e:
    print(e)
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
print(counter.current)
counter.step_down()
print(counter.current)
counter.step_down()
print(counter.current)
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7, 'Test4'
