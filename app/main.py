from fastapi import FastAPI
from app.optimizer import optimize

app = FastAPI(
    title="CPG Daily Marketing Optimizer",
    version="1.0.0",
    description="Daily marketing budget optimization for a CPG company"
)


@app.get("/")
def home():
    return {
        "application": "CPG Daily Marketing Optimizer",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/recommendations")
def recommendations():
    return optimize()