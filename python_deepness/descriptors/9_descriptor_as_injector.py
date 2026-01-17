# Deskryptor jako Injector (DI pattern)

class Service:
    def run(self):
        print("Running service logic.")

class InjectService:
    def __get__(self, instance, owner):
        return Service()  # "wstrzyknięcie" nowego serwisu


class Controller:
    service = InjectService()

    def handle(self):
        self.service.run()

c = Controller()
c.handle()  # Running service logic.
