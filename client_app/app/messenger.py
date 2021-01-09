import os
import json
import requests

from algorithm.elgamal import ElGamal


class Messenger():
    def __init__(self):
        self.elgamal = self.Init_ElGamal()

    def unpack_parameters(self, P, G, public_key):
        return P, G, public_key

    def Init_ElGamal(self):
        parameters = requests.get('http://middleware:8000/api/get-params')
        P, G, server_public_key = self.unpack_parameters(**parameters.json())
        elgamal = ElGamal(P, G)
        elgamal.Generate_Private_Key(server_public_key)
        print(elgamal.private_key)
        return elgamal

    def Send_Message(self, message):
        url = 'http://middleware:8000/api/get-inverse'
        encrypted_message = self.elgamal.Encrypt_Message(message)
        message_data = {
            'message': encrypted_message,
            'public_key': self.elgamal.public_key
        }
        message_data = json.dumps(message_data).encode('utf-8')
        response = requests.post(url, data=message_data)
        print(response.json())


def run():
    message = os.environ['MESSAGE']
    messenger = Messenger()
    messenger.Send_Message(message)
