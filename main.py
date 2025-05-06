from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# Hardcoded API key (not secure — only for personal/testing use)
genai.configure(api_key="AIzaSyAgiaMPYCvLQsvM15SV8gXL2o8tlRmDGMQ")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Create FastAPI app
app = FastAPI()

# Define request body structure
class PromptRequest(BaseModel):
	prompt: str

# Endpoint to generate response
@app.post("/generate")
async def generate_text(req: PromptRequest):
	try:
		response = model.generate_content(req.prompt)
		return {"response": response.text}
	except Exception as e:
		return {"error": str(e)}
