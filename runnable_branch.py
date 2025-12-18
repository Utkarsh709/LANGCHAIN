from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template="write a detailed explanation about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="give summary of {text} in less than 500 words",
    input_variables=['text']
)

model = ChatOpenAI()
parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x["text"].split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

report = report_gen_chain.invoke({"topic": "america"})
result = branch_chain.invoke({"text": report})

print(result)