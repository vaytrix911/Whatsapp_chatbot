from google import genai
from app.config import GEMINI_API_KEY
from google.genai.errors import ServerError
import time
client = genai.Client()


def get_agent_reply(user_message):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=user_message,
        )
            return response.text
        except ServerError:
            if attempt == 2:
                raise
            time.sleep(2)