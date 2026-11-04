import os
import json
import subprocess
from pathlib import Path

from agent import get_model_response

from openai import OpenAI
client = OpenAI()

running = True
while (running):
    user_input = input("""AI Coding Agent
    -------------------
    Enter your instructions: """)
    if (user_input.strip().lower() == "exit"):
        running = False
    elif (user_input.strip == ""):
        print("Enter a valid input")
        continue
    response = get_model_response(user_input)
    print(response)

