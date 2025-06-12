import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_input = sys.argv
    verbose = False

    if len(user_input) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    if user_input[-1] == "--verbose":
        verbose = True
        user_prompt = " ".join(user_input[1:-1])
    else:
        user_prompt = " ".join(user_input[1:])

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
    )

    if verbose:
        print(f'"User prompt: {messages[0].parts[0].text}"')
        print(f'"Prompt tokens: {response.usage_metadata.prompt_token_count}"')
        print(f'"Response tokens: {response.usage_metadata.candidates_token_count}"')
        print(response.text)
    else:
        print(response.text)

if __name__ == "__main__":
    main()