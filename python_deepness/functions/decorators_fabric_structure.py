
from functools import wraps


def decorator_fabric(dec_arg):
    # 1. Poziom: Fabryka - przyjmuje argumenty dekoratora

    def decorator(f):
        # 2. Poziom: Właściwy dekorator - przyjmuje tylko funkcję 'f'

        @wraps(f)
        def wrapper(*args, **kwargs):
            # 3. Poziom: Wrapper - tutaj mamy dostęp do 'dec_arg' (z domknięcia)
            print(f"Używam argumentu dekoratora: {dec_arg}")
            return f(*args, **kwargs)

        return wrapper


    print("Cześć!")


hello()


#
#
# Alternatywa: Klasa jako dekorator
# Jeśli trójpoziomowe funkcje wydają Ci się mało czytelne, na poziomie Senior często stosuje się klasy z metodą __call__:

# class DecoratorFabric:
#     def __init__(self, dec_arg):
#         self.dec_arg = dec_arg
#
#     def __call__(self, f):
#         @wraps(f)
#         def wrapper(*args, **kwargs):
#             print(f"Logika z argumentem: {self.dec_arg}")
#             return f(*args, **kwargs)
#         return wrapper

