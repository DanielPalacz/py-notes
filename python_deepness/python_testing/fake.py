class FakeDatabase:
    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key, None)


# Usage in a test
fake_db = FakeDatabase()
fake_db.save("user1", {"name": "Alice"})
assert fake_db.get("user1") == {"name": "Alice"}
