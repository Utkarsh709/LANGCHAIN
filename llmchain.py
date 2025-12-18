from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API keys


llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

prompt = PromptTemplate(
    input_variables=['topic'],
    template="Suggest a catchy blog title about {topic}"
)

chain = LLMChain(llm=llm, prompt=prompt)

topic = input('Enter a topic: ')
output = chain.invoke({"topic": topic})

print("Generated blog title:", output['text'])
