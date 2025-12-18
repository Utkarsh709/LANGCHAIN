from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="explain this joke: {joke}",
    input_variables=['joke']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain1 = RunnableSequence(prompt1, model, parser)
chain2 = RunnableSequence(prompt2, model, parser)

joke = chain1.invoke({'topic': 'laptop'})
explanation = chain2.invoke({'joke': joke})

print("Joke:", joke)
print("\nExplanation:", explanation)