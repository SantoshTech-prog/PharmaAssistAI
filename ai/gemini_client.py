import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


def generate_explanation(prompt: str) -> str:
    """
    Sends the prompt to Gemini and returns
    the generated explanation.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY was not found in the .env file."
        )

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text


if __name__ == "__main__":

    test_prompt = """
Explain why a member must submit Prior Authorization
even though the medication is covered.
"""

    explanation = generate_explanation(test_prompt)

    print(explanation)