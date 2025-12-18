from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a 5-pointer summary from the following text:\n{text}",
    input_variables=["text"]
)

model = ChatOpenAI()
parser = StrOutputParser()


to_dict = RunnableLambda(lambda x: {"text": x})


chain = prompt1 | model | parser | to_dict | prompt2 | model | parser


result = chain.invoke({"topic": "interesting facts about India"})
print("\nFinal Output:\n", result)


chain.get_graph().print_ascii()
