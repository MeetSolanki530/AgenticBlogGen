import uvicorn
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from src.graphs.graph_builder import GraphBuilder
from src.llms.groq_llm import GroqLLM

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

### API's


@app.get("/")
def get_home():
    return JSONResponse(content={"response" :"API WORKING PROPERLY"},status_code=200)

@app.post("/blogs")
async def create_blogs(request:Request):
    
    data = await request.json()

    topic = data.get("topic","")
    language = data.get("language")

    ### get the llm object

    groqllm = GroqLLM()
    
    llm = groqllm.get_llm()

    ## get the graph

    graph_builder = GraphBuilder(llm=llm)

    if topic and language:
        graph=graph_builder.setup_graph(usecase="language")
        state = graph.invoke({"topic" : topic,"current_langauge" : language})

    if topic:
        graph=graph_builder.setup_graph(usecase="topic")
        state = graph.invoke({"topic" : topic})
    
    
    return {"data":state}

if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)



