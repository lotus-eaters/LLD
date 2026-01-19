# First call: Logger()
#   ↓
# __new__(Logger):  # cls = <class 'Logger'>
#   if None → YES
#   cls._instance = object.__new__(Logger)  # Creates: <__main__.Logger object>
#   return cls._instance
  
# Second call: Logger()
#   ↓
# __new__(Logger):
#   if None → NO  
#   return cls._instance  # Returns EXISTING object

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating logger instance")
            cls._instance = super().__new__(cls)
        else:
            print("Returning existing one")
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            print("Initializing logger")
            self.log_file = open("app.log", "a")
            self.initialized = True

    def log(self, message):
        self.log_file.write(message + "\n")
        self.log_file.flush()


print("Creating logger1:")
logger1 = Logger()

print("\nCreating logger2:")
logger2 = Logger()

print("\nCreating logger3:")
logger3 = Logger()

print("\nAre they the same?",
      logger1 is logger2 is logger3)

logger1.log("Message from logger1")
logger2.log("Message from logger2")
logger3.log("Message from logger3")
