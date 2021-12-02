from enum import Enum
from fastapi import FastAPI

app = FastAPI(host='0,0,0,0',port=8002)

class Informations(str , Enum):
    capteur = "capteur"

@app.get("/api")
def api_root():
        return {"welcome to": "Raspi_API"}

@app.get("/api/info")
async def get_info():
        return {"name": "raspi jardin",
                "capteur": ["temp", "hum", "light", "presence"],
                "switch": ["pompe", "lumière", "vanne1", "vanne2"]}

