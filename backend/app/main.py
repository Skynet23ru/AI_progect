from fastapi import FastAPI

app = FastAPI(title="Fleet Management API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Fleet Management API is running", "status": "operational"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}