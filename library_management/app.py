from library_management.infrastructure.db_adapter import InMemoryBookRepository
from library_management.core.services import LibraryService
from library_management.infrastructure.api_adapter import create_app

# Initialisation of repository and service
repository = InMemoryBookRepository()
service = LibraryService(repository)

# Creating app
app = create_app(service)

if __name__ == "__main__":
    app.run(debug=True)

