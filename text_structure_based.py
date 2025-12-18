from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
India is a diverse and culturally rich country located in South Asia, known for its vast history, traditions, and rapid economic growth. It is the seventh-largest nation by land area and the most populous country in the world, with over 1.4 billion people. India is a federal democratic republic with 28 states and 8 union territories, governed under the framework of the Constitution of India. The capital city is New Delhi, while Mumbai is the financial hub. India boasts a rich cultural heritage, reflected in its festivals, languages, arts, and cuisine. It is the birthplace of major religions like Hinduism, Buddhism, Jainism, and Sikhism. The Indian economy is among the fastest-growing globally, driven by sectors like information technology, agriculture, manufacturing, and services. Despite its progress, India faces challenges such as poverty, unemployment, and infrastructure development, yet it remains a global powerhouse in technology, science, and space exploration.

"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,  
    chunk_overlap=0,  
    separator=' '  
)

result = splitter.split_text(text)
print(result)