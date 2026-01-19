# The Dependency Inversion Principle (DIP), the final SOLID principle, states that high-level modules 
# should not depend on low-level modules; both should depend on abstractions, and abstractions should 
# not depend on details—details should depend on abstractions. ​

# Core Idea
# High-level policy code relies on stable abstractions rather than volatile concrete implementations, 
# inverting traditional dependencies. This decouples components, making systems more flexible and testable

from abc import ABC,abstractmethod
class Logger(ABC):
    @abstractmethod
    def log(self,message):
        pass

class FileLogger(Logger):
    def log(self,message):
        with open('app.log','a') as f:
            f.write(f'{message}\n')

class ConsoleLogger(Logger):
    def log(self,message):
        print(f'[LOG],{message}')

class CloudLogger(Logger):
    def log(self, message):
    # Send to cloud service
        print(f"[CLOUD] {message}")

class UserService:
    def __init__(self,logger:Logger):
        self.logger=logger
    
    def create_user(self,username):
        print(f"Creating user: {username}")
        self.logger.log(f"User created: {username}")

file_logger = FileLogger()
console_logger = ConsoleLogger()
cloud_logger = CloudLogger()

# Development
dev_service = UserService(console_logger)
dev_service.create_user("john")

# Production
prod_service = UserService(cloud_logger)
prod_service.create_user("jane")

# Testing
class MockLogger(Logger):
    def __init__(self):
        self.messages = []
    
    def log(self, message):
        self.messages.append(message)

mock = MockLogger()
test_service = UserService(mock)
test_service.create_user("test_user")
print(f"Logged messages: {mock.messages}")



