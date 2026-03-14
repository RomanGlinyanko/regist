from fastapi import APIRouter

route = APIRouter()

@route.get('/mat/')
async def mat():
    ...

@route.get('/mat/def')
async def mat_def():
    ...