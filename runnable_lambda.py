"""
from langchain.schema.runnable import RunnableLambda
def word_counter(text):
    return len(text.split())
runnable_word_counter=RunnableLambda(word_counter)
result=runnable_word_counter.invoke("when the co2 contain the atmosphere")
print(result)
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough, RunnableSequence, RunnableParallel

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)

model = ChatOpenAI()
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'mobile'})

print("Joke:", result['joke'])
print("Word Count:", result['word_count'])