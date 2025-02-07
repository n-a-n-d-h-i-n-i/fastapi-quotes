import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (Fix for Axios requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway!"}

@app.get("/quote")
def get_quote():
    return {"quote": "AI will not replace you, but someone using AI will."}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Railway assigns a dynamic PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
