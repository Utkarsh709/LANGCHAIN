from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="generate a tweet for following {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="generate a linkedin post for following {text}",
    input_variables=['text']
)

model = ChatOpenAI()
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'text': 'AI'})

print("Tweet:", result['tweet'])
print("\nLinkedIn Post:", result['linkedin'])