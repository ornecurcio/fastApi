from fastapi import FastAPI, Path, Query, status, HTTPException
from gtts import gTTS
import numpy as np
from pydantic import BaseModel

# instalar en el entorno virtual 
# pip install fastapi
# pip install gTTs
# pip install requests
# pip install numpy
# pip install "uvicorn[standard]" 

# to run app es:  uvicorn nombre_archivo:app --reload

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def item(item_id: int):
    return {"item_id": item_id}

@app.get("/rand/{max}")
def rand(min: int = 0, max: int = 10):
    return f'Random number: {np.random.randint(min+1, max+1)}'

class Item(BaseModel):
    name: str
    price: float

@app.post("/create")
def create_item(item: Item):
    return f"New item created with name {item.name} and price {item.price}."

@app.post("/cambalache/{number}")
def cambalache(item: Item, number: int = Path(ge=4), q: str = Query("query", title="Algun param",
min_length=3)):
    result = {"number": number, "query": q, **item.dict()}
    return result

items = {1: "Item nro 1", 3: "Item nro 3"}
@app.get("/item/{item_id}", status_code=status.HTTP_201_CREATED)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


class Texto(BaseModel):
    text: str
@app.post("/texto")
def create_item(item: Texto):
    tts = gTTS(item.text)
    tts.save('test.mp3')
    return f"New mp3 file create from {item.text}"

#     >>> 
# >>> tts = gTTS('hello')
# >>> tts.save('hello.mp3')
    