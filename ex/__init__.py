import asyncio
from aiohttp import web

class Ex:
    def __init__(self):
        self._loop = asyncio.get_event_loop()
        self._app = web.Application(loop=self._loop)

    def listen(self, host='127.0.0.1', port=8000):
        self._loop.run_until_complete(self._loop.create_server(self._app.make_handler(), host, port))
        try:
            self._loop.run_forever()
        except KeyboardInterrupt:
            print("Ctrl + C pressed and quit.")

    def head(self, path):
        return self.verb('HEAD', path)

    def get(self, path):
        return self.verb('GET', path)

    def post(self, path):
        return self.verb('POST', path)

    def delete(self, path):
        return self.verb('DELETE', path)

    def put(self, path):
        return self.verb('PUT', path)
    
    def verb(self, verb, path):
        def v(handle):
            self._app.router.add_route(verb, path, asyncio.coroutine(handle))
        return v


