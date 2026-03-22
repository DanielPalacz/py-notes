

from functools import wraps

def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

# Function decorators
# 1. Closure (to robi Python / interpreter)
#    Python musi utworzyć __closure__
#    f musi być free variable
#       bez tego wrapper nie ma dostępu do oryginalnej funkcji

# 2. *args, **kwargs
#    odpowiedzialność Usera

# 3. @wraps(f)
#    to jest dodatkowa funkcjonalność zapewniona przez functools.wraps
#    @wraps(f) kopiuje metadane (__name__, __doc__, __qualname__, __annotations__) i nie dotyka __closure__
#    @wraps(f) dodaje __wrapped__ (ustawia wrapper.__wrapped__ = f)


    #  - f pochodzi z enclosing scope i f → free variable,
    #  - Python tworzy cell - cell trafia do wrapper.__closure__,
    #  - Gdyby closure nie istniało, wrapper nie miałby jak wywołać f.
    #  - Python wymusza closure, ale nie wymusza poprawnego dekoratora — to zadanie developera.