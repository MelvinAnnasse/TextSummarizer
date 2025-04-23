from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textSummarizer.pipeline.stage5_prediction_pipeline import PredictionPipeline
from fastapi.middleware.cors import CORSMiddleware
import pydantic



text:str = "What is Text Summarization?"

app = FastAPI()

# Allow your frontend origin (adjust to your frontend's URL)
origins = [
    "http://localhost:5000",  # if your frontend runs on localhost:5000
    "http://127.0.0.1:5000",
    "http://0.0.0.0:5000",  

    # add production domains too if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],    # Allow all HTTP methods
    allow_headers=["*"],    # Allow all headers
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    



from pydantic import BaseModel

class RequestBody(BaseModel):
    text: str

@app.post("/predict")
async def predict_route(body: RequestBody):
    try:
        obj = PredictionPipeline()
        result = obj.predict(body.text)
        return {"summary": result}
    except Exception as e:
        return {"error": str(e)}
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
