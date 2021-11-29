from enum import Enum
from fastapi import FastAPI

app = FastAPI(host='0,0,0,0',port=7000)

class Informations(str , Enum):
    name = "name"
    online = "online"
    capteur = "capteur"

@app.get("/api")
def api_root():
        return {"welcome to": "Raspi_API"}

@app.get("/api/infos/{info_item}")
async def get_info(info_item: Informations):
    if info_item == "name":
        return {"raspy_name": "test module"}
    if info_item == "online":
        return {"raspy_conected": True}
    else:
        return {"info requested": info_item}

