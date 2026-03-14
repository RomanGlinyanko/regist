from fastapi import APIRouter, Query

route = APIRouter()

@route.get('/clx/')
async def clx(id:int = Query(description = 'Идентификатор', title = 'ID')): #Query Parameters (@route.get('/clx/{id}') - Path Parameters)
    return {'id':{id}} 

@route.post('/clx/bar/')
async def clx_bar_post(id:int):
    ...

@route.get('/clx/bar/')
async def clx_bar():
    ...    