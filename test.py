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

print("=" * 40)
print("      Gemini API Test")
print("=" * 40)

while True:
    prompt = input("\nEnter your prompt (or type 'exit'): ")

    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    success = False

    # Retry up to 3 times
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            print("\nAI Response:")
            print("-" * 40)
            print(response.text)
            print("-" * 40)

            success = True
            break

        except Exception as e:
            print(f"\nAttempt {attempt + 1} failed.")

            if attempt < 2:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("\nError:", e)

    if not success:
        print("\nPlease try again later.")