from sanic import Sanic
from sanic.response import json

app = Sanic("my-hello-world-app")

@app.route('/abc')
async def test(request):
    return json({'hello': 'world'})
