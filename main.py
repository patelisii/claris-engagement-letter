from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from python.generate import generate_letter
from python.generate import add_letter_to_db


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    inputs: dict

@app.post("/createEngageLetter/")
async def receive_dictionary(item: Item):
    if not item.inputs:
        raise HTTPException(status_code=400, detail="No provisions provided")
    engagementLetterText = generate_letter(item.inputs)
    add_letter_to_db(item.inputs)
    return {"data": engagementLetterText}
