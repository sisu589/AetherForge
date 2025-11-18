import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Env
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():
    # Parse arguments
    user_prompt = sys.argv[1] if len(sys.argv) > 1 else ""
    # Verbose
    verbose = "--verbose" in sys.argv
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
    )
    
    usage = response.usage_metadata
    print(response.text)
    
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")

if __name__ == "__main__":
    main()
    