from __future__ import annotations


from flask import Flask


app = Flask(__name__)

def home() -> str:
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Flask App</title>
        </head>
        <body>
            <h1>Hello!</h1>
            <h1 style="margin: 20px">I am Flask app...</h1>
        </body>
    </html>
    """

app.add_url_rule("/", view_func=home, methods=("GET",))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0", port=7777)
