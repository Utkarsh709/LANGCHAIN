from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")


llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",  
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    temperature=0.7,
    max_new_tokens=200
)

model = ChatHuggingFace(llm=llm)

st.header('Research Tool')

paper_input=st.selectbox("Research Paper Name",["Attention Is All You Need","BERT:Pre-training of Deep Bidirectional Transformers",
"GPT-3:Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])
style_input=st.selectbox("Select Explanation Style",["Begineer_Friendly","Technical","Code-Oriented","Mathematical"])
length_input=st.selectbox("Select Explanation Length",["Short (1-2 paragraph)","Medium (3-5 paragraph)","Long (detailed Explanation)"])

template=PromptTemplate(
    template="""
    please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style:{style_input}
    Explanation Length:{length_input}
    1.Mathematical Details:
      -Include relevant mathematical equations if present in the paper
      -Explain the mathematical concepts using simple,intuitive code snippets where
      applicable.
    2.Analogies:
     -Use relatable analogies to simplify complex ideas.
    If certain information is not available in the paper,respond with:"Insufficient Information available"
    instead of guessing.
    Ensure the summary is clear ,accurate,and alligned with the provided style and length. 
    
    """,
    input_variables=['paper_input','style_input','length_input']
    
)

prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
