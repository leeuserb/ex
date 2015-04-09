# Ex
Take the express(ive) to the Python Web Development!

For now, it's just:

```python
from aiohttp import web
from ex import Ex

app = Ex()

@app.get('/')
def index(request):
  return web.Response(body='Hello World!'.encode('utf-8'))

app.listen()
```

The way:
* No explicit aiohttp APIs.
* Auto reload when developing.
* JSON response by native.
* A template system, maybe...
