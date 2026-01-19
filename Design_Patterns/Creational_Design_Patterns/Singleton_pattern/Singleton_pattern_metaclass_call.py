class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):  # ← Runs when MyClass()
        print(f"Creating instance of {cls.__name__}")
        
        if cls not in cls._instances:
            # Create instance
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass

db1 = Database()  # SingletonMeta.__call__ → Creates
db2 = Database()  # SingletonMeta.__call__ → Returns cached
print(db1 is db2)  # True!

# | Object    | obj() calls      | Example         |
# | --------- | ---------------- | --------------- |
# | Instance  | obj.__call__()   | CallableClass() |
# | Class     | Class.__call__() | MyClass()       |
# | Metaclass | type.__call__()  | MyMeta()        |

# "__call__() makes objects callable. For instances: obj() → obj.__call__(). For classes: MyClass() → metaclass __call__() → __new__() → __init__(). Used for Singletons, decorators, counters."

# TLDR: __call__() = function syntax for objects. obj() → obj.__call__()!


