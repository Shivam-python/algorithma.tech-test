from aiohttp import web
import socketio
import os,sys

s_io = socketio.AsyncServer() # creating async server
web_app = web.Application() # to create web application
s_io.attach(web_app)

# Running server
async def index(request):
    with open(os.path.join(sys.path[0], 'index.html')) as f:
        return web.Response(text=f.read(), content_type='text/html')

@s_io.on('msg') # will work when msg sent from client
async def print_message(sid, message):
    """
    This function will return msg received from client in reverse form
    """
    await s_io.emit('message', "reverse is - "+message[::-1]) # sending in message key

# created routes for accessing our client web page
web_app.router.add_get('/', index)

# program will start from here
if __name__ == '__main__':
    web.run_app(web_app)