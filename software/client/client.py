import socketio
import json
from btn_input import Buttons

sio = socketio.Client()

class Client:

    def __init__(self):
        self.btn = None

    def send_input_key_event(self, channel):

        # input_key = retrieve_values(self.btn.pins[channel])
        input_key = self.btn.retrieve_values(channel)

        try:
            sio.emit('received_input', {'pin_obj': input_key})
            print('sent ', input_key)
        except Exception as e:
            print(e)

    def send_sensor_readings(self):
        while True:
            sio.emit('my_message', {'temp':75})
            sio.sleep(5)

    def start_client(self):

        pins = [26, 16, 12, 25, 24, 23]
        self.btn = Buttons(pins)
        self.btn.set_pin_callback(self.send_input_key_event)
        
        # print(self.btn.pins)

        with open('./data/client_config.json') as f:
            client_config = json.load(f)

        sio.connect(client_config["server_address"], headers=client_config["headers"])

    def reconnect(self):
        sio.connect(client_config["server_address"], headers=client_config["headers"])


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

# Old implementation
# def retrieve_values(object):
#   return (object.pin, object.is_active, object.is_virtual)


if __name__ == "__main__":
    # sio.connect(client_config["server_address"], headers=client_config["headers"])
    pi_client = Client()
    pi_client.start_client()