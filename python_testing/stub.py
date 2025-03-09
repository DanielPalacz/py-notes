class DatabaseStub:
    def get_user(self, user_id):
        # Instead of calling an actual database, this returns a predefined value.
        return {"id": user_id, "name": "John Doe"}


# Usage in a test:
db_stub = DatabaseStub()
assert db_stub.get_user(1) == {"id": 1, "name": "John Doe"}
