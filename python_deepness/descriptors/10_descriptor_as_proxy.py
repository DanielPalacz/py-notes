class Proxy:
    def __init__(self, target_name):
        self.target_name = target_name  # np. 'real'

    def __get__(self, instance, owner):
        real_obj = getattr(instance, self.target_name)
        return real_obj.value  # proxy to .value

    def __set__(self, instance, value):
        real_obj = getattr(instance, self.target_name)
        real_obj.value = value


class Target:
    def __init__(self):
        self.value = 42

class Wrapper:
    real = Target()
    proxy = Proxy('real')

w = Wrapper()
print(w.proxy)     # 42
w.proxy = 100
print(w.real.value)  # 100
