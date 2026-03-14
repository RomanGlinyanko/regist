from fastapi import FastAPI
from .routes import lst_routers

app = FastAPI(title = 'REGIST')

@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в API REGIST",
        "docs": "/docs"
    }

for route in lst_routers:
    app.include_router(route)

