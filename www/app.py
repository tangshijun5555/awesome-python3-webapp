import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    ''' 一个处理函数，返回带HTML代码的响应 '''

    #charset=utf-8是设置页面内容为网页编码，不然部分浏览器会直接将不严格的HTTP头当文件下下来
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

async def init(loop):
    ''' 服务器运行程序：创建web实例，该实例绑定路由和处理函数，运行服务器，监听端口请求，送到路由处理 '''
    app = web.Application(loop=loop)

    #GET表示一个读取请求，将从服务器获得网页数据，/表示URL的路径，URL总是以/开头，/就表示首页，
    app.router.add_route('GET', '/', index) 
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

#创建异步框架的事件轮询实例
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()