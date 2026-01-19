# logger.py (a module file)

class _Logger:
    """Private logger class"""
    def __init__(self):
        print("Initializing logger")
        self.log_file = open('app.log', 'a')
    
    def log(self, message):
        self.log_file.write(f"{message}\n")
        self.log_file.flush()


# Create single instance at module level
logger = _Logger()


# main.py
from logger import logger  # Import the singleton instance

logger.log("Message 1")
logger.log("Message 2")


# another_file.py
from logger import logger  # Same instance!

logger.log("Message 3")