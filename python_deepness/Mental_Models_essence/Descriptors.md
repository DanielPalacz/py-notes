## Deskryptory — plan operacyjnego opanowania (80%)

```
Czym są i jak działają (data / non-data / fallback). Model mentalny:
    1)
    attribute lookup krok po kroku z deskryptorem
    __get__, __set__, __delete__ — kiedy i jak się aktywują
    2)
    Deskryptor vs zwykła instancja / property / metoda
    3)
    Deskryptor w klasie bazowej a nadpisanie w podklasie
    4)
    Deskryptory + super() + metaklasy
    5)
    Deskryptory a __set_name__, __slots__, cacheowanie
    
    6)
    Zastosowania: property, @classmethod, validation fields, lazy loading, ORM
```

## Natura deskryptorów:
```
 - One są bardzo techniczne, nie są często stosowane mają konkretny / rzadki / specjalistyczny use-case.
 - Uczą się ich często osoby piszące frameworki, ORM-y, API do komponentów.
 - Większość devów korzysta z efektów deskryptorów (np. @property, @classmethod, dataclass.field()...), ale nie pisze ich samodzielnie.
```

### Difference between Data Descriptor vs Non-Data Descriptor
```
| Feature                      | Data Descriptor                             | Non-Data Descriptor                   |
| :--------------------------- | :------------------------------------------ | :------------------------------------ |
| Implements                   | `__get__` + (`__set__` or `__delete__`)     | Only `__get__`                        |
| Priority over instance dict? | **Yes, always wins**                        | **No, instance attribute wins**       |
| Common Use Cases             | type checking, enforcing read-only          | computed attributes (like properties) |
| Example                      | `@property` with setter, `@cached_property` | Simple `@property` without setter     |

```

### Descriptors repetition questions:
```
1. What exactly is a descriptor in Python? Can you give a short technical definition?
2. What's the difference between a data descriptor and a non-data descriptor?
3. When is __get__ called? What arguments does it receive?
4. If an instance’s __dict__ has an attribute of the same name as a non-data descriptor in the class, which one takes precedence?
5. How would you implement a descriptor that makes an attribute read-only after it's been set once?
6. Why does property use the descriptor protocol internally? What benefits does it get from it?
7. Can a method in a class (like a normal function defined inside a class) act as a descriptor? Why or why not?
```
