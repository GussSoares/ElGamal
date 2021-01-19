import json
import requests
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel
from middleware_app.algorithm.elgamal import ElGamal


def Generate_Parameters_PG():
    P = 59399
    G = 59333
    return P, G


def Get_Inverse_From_Server(message):
    url = 'http://server:8888/api/get-inverse'
    message_data = {
        'message': message
    }
    message_data = json.dumps(message_data).encode('utf-8')
    response = requests.post(url, data=message_data)
    return response.json()['Inverse_Message']


class Item(BaseModel):
    public_key: int
    message: str
    description: Optional[str] = None


router = APIRouter()
P, G = Generate_Parameters_PG()
middleware_elgamal = ElGamal(P, G)


@router.get('/get-params', tags=['api'])
async def get_params():
    return {
        'P': P,
        'G': G,
        'public_key': middleware_elgamal.public_key
    }


@router.post('/get-inverse', tags=['api'])
async def get_inverse(item: Item):
    # middleware_elgamal.Generate_Private_Key(item.public_key)
    decrypted_message = middleware_elgamal.Decrypt_Message(
                            item.public_key,
                            item.message)
    decrypted_message = Get_Inverse_From_Server(decrypted_message)

    return {
        'Inverse_Message': decrypted_message
    }
