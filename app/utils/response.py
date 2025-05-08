import os

import google.generativeai as genai
from dotenv import load_dotenv

from app.utils.settings import Constants

load_dotenv()
api_key = os.getenv("GOOGLE_GEMINI_API")

genai.configure(api_key=api_key)


def gemini_response(context) -> str:
    prompt = Constants.GEMINI_PROMPT.format(context)
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    r = model.generate_content(prompt)
    return r.text
