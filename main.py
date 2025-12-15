from fastapi import FastAPI

app = FastAPI()


@app.post("/alarme")
def criar_alarme(hora: int, minuto: int, label: str = "Alarme"):
    return {
        "hora": hora,
        "minuto": minuto,
        "label": label
    }
