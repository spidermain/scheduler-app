from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "✅ App is live!"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("🔔 Webhook received:", data)
    return {"status": "received", "data": data}
