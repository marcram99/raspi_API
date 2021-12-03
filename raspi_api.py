from enum import Enum
from fastapi import FastAPI

app = FastAPI(host='0,0,0,0',port=8001)

class Informations(str , Enum):
    capteur = "capteur"

@app.get("/api")
def api_root():
        return {"welcome to": "Raspi_API"}

@app.get("/api/info")
async def get_info():
        return {"name": "raspi cave",
                "capteur": ["temp", "hum", "light", "mov"],
                "switch": ["garage", "voiture", "pompe", "vanne1", "vanne2"]}

@app.get("/api/capteurs")
async def get_capteurs():
    # create capteur reading function...
    capteurs = {"temp": 22.05,
                "hum": 78,
                "lux": 122,
                "light": "dark",
                }
    return capteurs


