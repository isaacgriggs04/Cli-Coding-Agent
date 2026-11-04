from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def get_model_response(user_input):
    response = client.responses.create(
        model="gpt-6-luna",
        input = user_input
    )
    return response.output_text