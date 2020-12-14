import socketio
import json
from btn_input import Buttons

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    # sio.start_background_task(send_sensor_readings)

@sio.event
def disconnect():
    print('disconnected from server')

# For receiving Data from server
# @sio.event
# def my_message(data):
#     print('message received with ', data)
#     # sio.emit('my response', {'response': 'my response'})
#     # sio.sleep(5)    

# def btn_callback(self, channel):
#     print('button pressed {}'.format(channel))

def send_input_key_event(channel):
    # if connected:
        # sio.emit()
    print('button pressed {}'.format(channel))

def send_sensor_readings():
    while True:
        sio.emit('my_message', {'temp':75})
        sio.sleep(5)


def start_client():

    pins = [26, 16, 12, 25, 24, 23]
    btn = Buttons(pins)
    btn.set_pin_callback(send_input_key_event)

    with open('./data/client_config.json') as f:
        client_config = json.load(f)

    sio.connect(client_config["server_address"], headers=client_config["headers"])

def reconnect():
    sio.connect(client_config["server_address"], headers=client_config["headers"])

if __name__ == "__main__":
    # sio.connect(client_config["server_address"], headers=client_config["headers"])
    start_client()