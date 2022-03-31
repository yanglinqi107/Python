import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mysql import Db

app = FastAPI()
db = Db('tft')

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Hello, world!"


@app.get("/database/resume")
def resume():
    data = db.resume()
    return data


################################################## cards ###########################################
@app.get("/cards/all")
def getAll():
    data = db.getAll()
    return data


@app.get("/cards/search/name/")
def search(name: str):
    data = db.getItems(name)
    return data


@app.get('/cards/search/price/')
def searchByPrice(price: int):
    data = db.getItemsByPrice(price)
    return data


@app.get('/cards/search/fetters/')
def searchByFetter(fname: str):
    data = db.getItemsByFetter(fname)
    return data


@app.get("/cards/delete/")
def delete(id: int):
    data = db.delete(id)
    return data


@app.get("/cards/")
def read_card(id: int):
    data = db.getCard(id)
    return data


################################################## users ############################################
@app.get("/users/login/")
def getUser(id: str, pwd: str):
    data = db.getUser(id, pwd)
    return str(data)


@app.get("/users/register/")
def addUser(id: str, pwd: str):
    data = db.addUser(id, pwd)
    return data


if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host='127.0.0.1',
                port=8000,
                reload=True,
                debug=True)
