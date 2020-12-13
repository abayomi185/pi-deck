import eventlet
import socketio
# from wsgi import app

static_files = {
    '/': './data/server_config',
}

sio = socketio.Server()
# For development use only
# app = socketio.ASGIApp(sio, static_files=static_files)
app = socketio.WSGIApp(sio)

# sid - session id, a unique identifier for client connection

def get_device_id(environ):
    return environ.get('HTTP_DEVICE_ID', None)

#Special event connect and disconnect

@sio.event
def connect(sid, environ):
    device_id = get_device_id(environ) or sid
    # print(environ)
    sio.save_session(sid, {'device_id': device_id})
    print('{} is connected'.format(device_id))
    #user authentication and such; establishment protocols

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def my_message(sid, data):
    session = sio.get_session(sid)
    print('Received data from {}, {}'.format(session['device_id'], data))

if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app, log_output=False)