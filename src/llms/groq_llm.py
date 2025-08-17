from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            os.environ["GROQ_API_KEY"] = self.groq_api_key = os.getenv("GROQ_API_KEY")
            os.environ["GROQ_LLM_MODEL"] = self.groq_llm_model = os.getenv("GROQ_LLM_MODEL")
            self.llm=ChatGroq(api_key=self.groq_api_key,model=self.groq_llm_model)
            return self.llm
        except Exception as e:
            raise ValueError(f"Error Occured with exception : {e}")
    
