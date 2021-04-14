from fastapi import APIRouter
from deta import Deta

deta = Deta()
db = deta.Base('db_name')

router = APIRouter(
    prefix='/apip/v2',
    tags=['API']
    )


@router.get('/route', status_code=201)
async def get_all_():
    result = next(db.fetch())
    return result
