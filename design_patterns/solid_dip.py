from abc import ABC, abstractmethod

# High-level abstraction
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Low-level implementation
class FileLogger(Logger):
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(message + "\n")

# Another implementation (e.g., cloud logger)
class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[LOG]: {message}")

# High-level module depending on abstraction
class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger  # depends on Logger abstraction

    def create_user(self, name):
        # ... logic to create user
        self.logger.log(f"User '{name}' created.")
