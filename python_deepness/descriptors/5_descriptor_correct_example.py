

class PositiveInt:
    def __set_name__(self, owner, name):
        self.name = name
        # self.private_name = '_' + name

    def __get__(self, instance, owner):

        if instance is None:
            return self

        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # print(f"Setting {self.name} = {value}")

        if value < 0:
            raise ValueError("Value must be positive.")

        instance.__dict__[self.name] = value

class Product:
    price = PositiveInt()
    quantity = PositiveInt()


#
# p = Product()
# p.price = 100
# p.quantity = 5
#
# print(p.price, p.quantity)   # 100 5
#
# p.price = -10                # ValueError
