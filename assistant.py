from google import genai
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_gemini(prompt):
    """
    Sends a prompt to Gemini and returns the response.
    Retries automatically for temporary failures.
    """

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:
            error = str(e)

            print(f"\nAttempt {attempt + 1} failed.")

            # Daily quota exceeded
            if "RESOURCE_EXHAUSTED" in error or "429" in error:
                return """
========================================
Daily Gemini API quota exceeded.

You have used today's free requests.

Please:
1. Wait for the quota to reset.
2. Or use another Gemini API Key.

========================================
"""

            # Invalid API key
            elif "API_KEY_INVALID" in error or "401" in error:
                return """
========================================
Invalid Gemini API Key.

Please check your .env file.

========================================
"""

            # Gemini server busy
            elif "503" in error or "UNAVAILABLE" in error:
                if attempt < 2:
                    print("Gemini server busy. Retrying in 5 seconds...\n")
                    time.sleep(5)
                else:
                    return """
========================================
Gemini servers are currently busy.

Please try again later.

========================================
"""

            # Other errors
            else:
                if attempt < 2:
                    print("Retrying in 5 seconds...\n")
                    time.sleep(5)
                else:
                    return f"Unexpected Error:\n{error}"