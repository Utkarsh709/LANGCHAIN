from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import WebBaseLoader
url="https://www.buybooksindia.com/murarirao-ghorpade-the-accidental-catalyst-behind-robert-clive-s-march-over-india--9780143472988-117736.htm"
loader=WebBaseLoader(url)
docs=loader.load()
prompt=PromptTemplate(
    template="answer the following {question} from {info}",
    input_variables=['question','info']
)

model=ChatOpenAI()
parser=StrOutputParser()

chain=prompt | model | parser
result=chain.invoke({'question':'who is author of the book','info':docs[0].page_content})
print(result)