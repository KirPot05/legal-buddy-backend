import google.generativeai as genai

genai.configure(api_key="AIzaSyC-zF-VYDMtN6i7Y3MiRodQ8DDJV8zCn64")

prompt = """

Indian Law. Extract a concise summary of the following case, detailing each relevant penal code and act, with their specific implications in this case:

Note: Use a language which is very simple for any person to understand. Also try to include the next possible steps to be taken in the case.
"""

model = genai.GenerativeModel("gemini-1.5-flash")


async def generate_summary(text: str) -> str:
    response = model.generate_content(prompt + text)
    return response.text
