def singleton(cls):
    """Decorator to make any class a singleton"""
    instances = {}  # Dictionary to store instances
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(f"Creating new instance of {cls.__name__}")
            instances[cls] = cls(*args, **kwargs)
        else:
            print(f"Returning existing instance of {cls.__name__}")
        return instances[cls]
    
    return get_instance


@singleton  # Apply decorator
class Logger:
    def __init__(self):
        print("Initializing logger")
        self.log_file = open('app.log', 'a')
    
    def log(self, message):
        self.log_file.write(f"{message}\n")
        self.log_file.flush()
        print(f"Logged: {message}")


# Testing
print("Creating logger1:")
logger1 = Logger()

print("\nCreating logger2:")
logger2 = Logger()

print(f"\nAre they the same? {logger1 is logger2}")

logger1.log("Hello from logger1")
logger2.log("Hello from logger2")

