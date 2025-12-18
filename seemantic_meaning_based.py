from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
text_splitter=SemanticChunker(
    OpenAIEmbeddings(),breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
    
)
sample="""
Farmers are the backbone of any nation, playing a vital role in producing food and sustaining the economy. In villages, agriculture is the primary occupation, and farmers work tirelessly in the fields to ensure a steady supply of crops. Despite their hard work, many farmers face challenges such as unpredictable weather, lack of modern equipment, and financial debts. Students in rural areas often experience difficulties in accessing quality education due to limited resources and infrastructure, yet they strive to learn and achieve their dreams. Villages, though rich in culture and tradition, sometimes lag in development, which impacts both farmers and students. Meanwhile, the threat of terrorism in certain regions creates an additional layer of insecurity, affecting livelihoods and education. Terrorism not only disrupts peace but also diverts resources that could otherwise be used for improving rural life. A strong, educated community with secure environments can help transform villages into hubs of progress, where farmers prosper, students succeed, and peace prevails.
"""
docs=text_splitter.create_documents([sample])
print(len(docs))
print(docs)
