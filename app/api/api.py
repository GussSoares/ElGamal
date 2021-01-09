from fastapi import APIRouter


router = APIRouter()

@router.get('/get-params', tags=['api'])
async def get_params():
    return {
        'param1': '1',
        'param2': '2'
    }
