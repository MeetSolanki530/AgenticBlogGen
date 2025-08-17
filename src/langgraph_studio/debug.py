from src.llms.groq_llm import GroqLLM
from src.graphs.graph_builder import GraphBuilder



## Below code is for the langsmith langgraph studio

llm = GroqLLM().get_llm()

## get the graph
graph_builder = GraphBuilder(llm)

graph = graph_builder.build_topic_graph().compile()
