from openai import OpenAI
from app.utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

# Set up the API key so openai can authenticate requests


def get_recommendation(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an expert advisor helping high school students choose university majors.",
            },
            {"role": "user", "content": prompt},
        ],
    )
    # Return only the content part of the response
    return response.choices[0].message.content
