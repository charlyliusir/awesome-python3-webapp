# 添加日志打印
import logging; logging.basicConfig(level=logging.INFO)


# 异步IO框架
import asyncio
# 异步HTTP框架
from aiohttp import web


def hello(request):
	return web.Response(body=b'<h1>Hello World</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('Get', '/', hello)
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9090)
	logging.info("server started at http://127.0.0.1:9090")
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()