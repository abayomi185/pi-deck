import eventlet
import socketio
import json
# from wsgi import app

static_files = {
    '/': './data/server_config',
}

with open('./data/server_config.json') as f:
  server_config = json.load(f)

sio = socketio.Server()
# For development use only
# app = socketio.ASGIApp(sio, static_files=static_files)
app = socketio.WSGIApp(sio)

def get_device_id(environ):
    return environ.get('HTTP_DEVICE_ID')

#Special event connect and disconnect
# sid - session id, a unique identifier for client connection

@sio.event
def connect(sid, environ):
    device_id = get_device_id(environ)
    # print(environ)
    # print(sid)
    # sio.save_session(sid, {'device_id': device_id})
    print('{} is connected'.format(device_id))
    #user authentication and such; establishment protocols

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def my_message(sid, data):
    # session = sio.get_session(sid)
    print('Received data from {}, {}'.format(sid, data))


def start_server():
    eventlet.wsgi.server(eventlet.listen(('', server_config["server_port"])), app, log_output=server_config["log_ouput"])


if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(('', server_config["server_port"])), app, log_output=server_config["log_ouput"])
    # eventlet.wsgi.server(eventlet.listen(('', 5000)), app)