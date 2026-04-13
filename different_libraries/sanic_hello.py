from sanic import Sanic
from sanic.response import json, text

app = Sanic("my-hello-world-app")

@app.get("/")
async def hello(request):
    return text("Hello, Sanic!")

@app.route('/abc')
async def test(request):
    return json({'hello': 'world'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
