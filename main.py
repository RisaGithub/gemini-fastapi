from fastapi import FastAPI, Query
from pydantic import BaseModel
import google.generativeai as genai

# Hardcoded API key (not secure — only for personal/testing use)
genai.configure(api_key="AIzaSyAgiaMPYCvLQsvM15SV8gXL2o8tlRmDGMQ")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Create FastAPI app
app = FastAPI()

# Define request body structure for POST
class PromptRequest(BaseModel):
	prompt: str

# Index route - shows available endpoints
@app.get("/")
async def index():
    return {
        "message": "Welcome to the Gemini FastAPI service!",
        "available_endpoints": [
            "/generate?prompt={your_prompt} (GET)",
            "/generate (POST) with JSON body {'prompt': 'your_prompt'}"
        ]
    }

# POST endpoint
@app.post("/generate")
async def generate_text_post(req: PromptRequest):
	try:
		response = model.generate_content(req.prompt)
		return {"response": response.text}
	except Exception as e:
		return {"error": str(e)}

# GET endpoint
@app.get("/generate")
async def generate_text_get(prompt: str = Query(..., description="Your prompt")):
	try:
		response = model.generate_content(prompt)
		return {"response": response.text}
	except Exception as e:
		return {"error": str(e)}
