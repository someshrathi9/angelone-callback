
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="Angel One Read Only Callback")

@app.get("/")
def home():
    return {
        "status": "online",
        "service": "Angel One Callback",
        "mode": "READ ONLY"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/callback")
async def callback(request: Request):
    # Never display or log authentication values.
    received = list(request.query_params.keys())

    return HTMLResponse(
        """
        <h2>Angel One Callback Received</h2>
        <p>Callback endpoint is working.</p>
        <p>Return to your application to continue.</p>
        """
    )
