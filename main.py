from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# fila simples em memória (suficiente pro free tier)
fila = []


@app.post("/alarme")
def criar_alarme(
    hora: int,
    minuto: int,
    label: str = "Alarme remoto"
):
    fila.append({
        "hora": hora,
        "minuto": minuto,
        "label": label
    })
    return {"status": "ok"}


@app.get("/alarme")
def pegar_alarme():
    if fila:
        return fila.pop(0)
    return {}
