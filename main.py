import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=google_api_key)

response = client.models.generate_content(
	model="gemini-2.0-flash",
	contents="Explica como funciona la inteligencia artificial detalladamente y con ejemplos"
)

print(response.text)
print("asd")