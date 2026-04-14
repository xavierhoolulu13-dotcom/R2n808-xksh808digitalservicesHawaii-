from fastapi import FastAPI
from src.core.orchestrator import Orchestrator

app = FastAPI()
orch = Orchestrator()

@app.post("/run")
def run(data: dict):
    return orch.run(data.get("workflow"), data.get("text"))
