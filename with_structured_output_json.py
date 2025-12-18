from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Literal
from pydantic import BaseModel, Field


load_dotenv()
model = ChatOpenAI()

class Summary(BaseModel):
    text: str = Field(description="A brief summary of the review")
    length: int = Field(description="Length of the summary")

class Review(BaseModel):
    summary: Summary = Field(description="Summary object containing text and length")
    sentiment: Literal['pos', 'neg', 'neutral'] = Field(description="Sentiment of the review")


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks
outdated compared to other brands. Hoping for a software update to fix this.
""")


print(result.json(indent=4))
print("\nSummary:", result.summary.text)
print("Length:", result.summary.length)
print("Sentiment:", result.sentiment)
