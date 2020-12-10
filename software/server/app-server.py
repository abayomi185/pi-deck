# import eventlet
import socketio
# from wsgi import app

static_files = {
    '/': './data/server_config',
}

sio = socketio.AsyncServer()
# For development use only
# app = socketio.ASGIApp(sio, static_files=static_files)
app = socketio.ASGIApp(sio)


# sid - session id, a unique identifier for client connection

@sio.event
def my_event(sid, data):
    pass

@sio.on('my custom event')
def another_event(sid, data):
    pass

@sio.event
async def my_event(sid, data):
    pass

#Special event connect and disconnect

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    #user authentication and such; establishment protocols

#Send data back to client in to indicate why connection failed

# @sio.event
# def connect(sid, environ):
#     raise ConnectionRefusedError('authentication failed')


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


#Send data to all connected clients

# sio.emit('my event', {'data': 'foobar'})

#Send data to a specific client

# sio.emit('my event', {'data': 'foobar'}, room=user_sid)

#Event callback to "return" information back to client

@sio.event
def my_event(sid, data):
    # handle the message
    return "OK", 123

#Namespaces

@sio.event(namespace='/chat')
def my_custom_event(sid, data):
    pass

@sio.on('my custom event', namespace='/chat')
def my_custom_event(sid, data):
    pass

#Namespaces can be given classes

class MyCustomNamespace(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        pass

    def on_disconnect(self, sid):
        pass

    async def on_my_event(self, sid, data):
        await self.emit('my_response', data)

sio.register_namespace(MyCustomNamespace('/test'))