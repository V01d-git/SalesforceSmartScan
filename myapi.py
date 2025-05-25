from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

from smartScan import impFunc
from smartScan import testFunc

app = FastAPI()
handler = Mangum(app)


class reqBody(BaseModel):
    ocrResult:str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/smart-scan")
async def scanFunc(reqBody:reqBody):
    return {"message": testFunc(reqBody.ocrResult)}