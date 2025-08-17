from langgraph.graph import StateGraph,START,END
from src.llms.groq_llm import GroqLLM
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    
    def __init__(self,llm):
        self.llm = llm
    
    def build_topic_graph(self):
        
        """
        Build a graph to generate blogs based on topic.
        """

        self.graph=StateGraph(BlogState)

        self.blog_node_obj = BlogNode(llm=self.llm)     
        print(self.llm)   

        ## Nodes
        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)


        ## Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation",END)

        return self.graph

    def build_langauge_graph(self):
        
        """
        Build Graph for blog generation with input topic and langauge 
        """
        self.graph=StateGraph(BlogState)


        self.blog_node_obj = BlogNode(llm=self.llm)     
        print(self.llm)   

        ## Nodes
        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)
        self.graph.add_node("hindi_translation",lambda state: self.blog_node_obj.translation({**state,"current_langauge":"hindi"}))
        self.graph.add_node("gujarati_translation",lambda state: self.blog_node_obj.translation({**state,"current_langauge":"gujarati"}))
        self.graph.add_node("route",self.blog_node_obj.route)

        ## edges and conditional edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation","route")

        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
            {
                "hindi" : "hindi_translation",
                "gujarati" : "gujarati_translation",
            }
            )
        self.graph.add_edge("hindi_translation",END)
        self.graph.add_edge("gujarati_translation",END)

        return self.graph
    
    def setup_graph(self,usecase):
        
        if usecase=="topic":
            self.build_topic_graph()
        
        if usecase=="language":
            self.build_langauge_graph()
        
        return self.graph.compile()
