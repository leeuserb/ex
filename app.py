from aiohttp import web
from ex import Ex

app = Ex()


@app.get('/')
def home(request):
	return web.Response(body='Hello World!'.encode('utf-8'));


app.listen()



