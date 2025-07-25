from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",    
    temperature=0.0,
    max_retries=2,
)

responce=llm.invoke("define love of mother?")
print("responce:",responce.content)
