from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow Next.js (frontend) to access FastAPI (backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = [
    "Believe in yourself!",
    "Stay positive, work hard, make it happen.",
    "Dream big and dare to fail.",
    "You are stronger than you think!",
]

@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}



