import socketio
from button import Buttons

sio = socketio.Client()

pins = [26, 16, 12, 25, 24, 23]
b = Buttons(pins)

# def send_input_key_event():
#     sio.emit()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})
    sio.sleep(5)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://10.0.1.3:5000', headers={'device_id':'cliet1'})