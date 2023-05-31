from fastapi import FastAPI, HTTPException
from spiritsol import generate_solution_snippet, generate_charities
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 32

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/generate_solution")
async def generate_solution_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_solution_snippet(prompt)
    return {"snippet": snippet, "charities": []}


@app.get("/generate_charities")
async def generate_charities_api(prompt: str):
    validate_input_length(prompt)
    charities = generate_charities(prompt)
    return {"snippet": None, "charities": charities}


@app.get("/generate_solution_and_charities")
async def generate_charities_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_solution_snippet(prompt)
    charities = generate_charities(prompt)
    return {"snippet": snippet, "charities": charities}


def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.",
        )
