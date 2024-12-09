
from flask import Flask, request, jsonify
from library_management.core.services import LibraryService

def create_app(library_service: LibraryService) -> Flask:
    app = Flask(__name__)

    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.json
        library_service.add_book(data['title'], data['author'], data['isbn'])
        return {"message": "Book added successfully"}, 201

    @app.route('/books', methods=['GET'])
    def list_books():
        books = library_service.list_books()
        return jsonify([book.__dict__ for book in books])

    return app
