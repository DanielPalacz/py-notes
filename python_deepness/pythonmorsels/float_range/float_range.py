
class F_Range:
    def __init__(self, start: float, end: float, step: float):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        x_tracker = self.start

        if self.step > 0:
            while x_tracker < self.end:
                yield x_tracker
                x_tracker += self.step

        elif self.step < 0:
            while x_tracker > self.end:
                yield x_tracker
                x_tracker += self.step

    def __len__(self):
        len_tracker = 0
        x_tracker = self.start

        if self.step > 0:
            while x_tracker < self.end:
                x_tracker += self.step
                len_tracker += 1

        elif self.step < 0:
            while x_tracker > self.end:
                x_tracker += self.step
                len_tracker += 1

        return len_tracker


    def __str__(self):
        if self.step - int(self.step) == 0:
            return f"float_range({self.start}, {self.end}, {int(self.step)})"
        else:
            return f"float_range({self.start}, {self.end}, {self.step})"

    def __repr__(self):
        if self.step - int(self.step) == 0:
            return f"float_range({self.start}, {self.end}, {int(self.step)})"
        else:
            return f"float_range({self.start}, {self.end}, {self.step})"



def float_range(start: float, end: float = None, step: float = 1.0):
    if end is None:
        end = start
        start = 0.0

    return F_Range(start, end, step)
