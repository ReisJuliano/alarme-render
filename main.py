from fastapi import FastAPI

app = FastAPI()

ultimo_alarme = None


@app.post("/alarme")
def criar_alarme(hora: int, minuto: int, label: str = "Alarme"):
    global ultimo_alarme
    ultimo_alarme = {
        "hora": hora,
        "minuto": minuto,
        "label": label
    }
    return ultimo_alarme


@app.get("/alarme")
def pegar_alarme():
    return ultimo_alarme
