from fastapi import APIRouter
from pydantic import BaseModel


class Item(BaseModel):
    message: str


router = APIRouter()


@router.post('/get-inverse', tags=['api'])
async def get_inverse(item: Item):
    message = item.message
    message = message[::-1]

    return {
        'Inverse_Message': message
    }
