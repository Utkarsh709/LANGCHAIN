from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))

while True:
    user_input = input('you: ')
    if user_input.lower() == 'exit':
        break

    result = model.invoke(user_input)
    print('AI:', result.content)
