from src.states.blog_state import BlogState
from langchain_core.messages import HumanMessage,SystemMessage
from src.states.blog_state import BlogState

class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self,llm):
        self.llm = llm
    
    ### Title Creation

    def title_creation(self,state:BlogState):
        
        """
        Create the title for the blog
        """

        if "topic" in state and state["topic"]:
            
            prompt="""
            You are an expert blog content writer. 
            User Markdown formatting.
            Generate a Blog title for the {topic}.
            This title should be creative and SEO Friendly.
            """

            system_message=prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return { "blog" : {"title" : response.content}}
        

    def content_generation(self,state:BlogState):
        """
        Create the content for blog
        """

        if "topic" in state and state["topic"]:
            
            system_prompt="""
            You are an expert blog content writer. 
            User Markdown formatting.
            Generate detailed Blog content with the detailed breakdown for the {topic}.
            """

            system_message=system_prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return { "blog" : {"title" : state["blog"]["title"],"content" : response.content}}
    
    def translation(self,state:BlogState):
        """
        Tranlate the content to specified langauge.
        """

        translation_prompt = """
        Translate the following content into {current_langauge}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_langauge}.

        ORIGINAL CONTENT:
        {blog_content}

        """

        blog_content = state['blog']['content']
        messages = [
            HumanMessage(translation_prompt.format(current_langauge=state["current_langauge"],blog_content=blog_content))
        ]

        translation_content = self.llm.with_structured_output(BlogState).invoke(messages)
        return {"blog": {"content": translation_content}}




    def route(self,state:BlogState):
        return {"current_langauge" : state["current_langauge"]}
    
    def route_decision(self,state:BlogState):
        
        """
        Route the content to the respective translation function.
        """

        if state["current_langauge"] == "hindi":
            return "hindi"
        elif state["current_langauge"] == "gujarati":
            return "gujarati"
        else:
            return state["current_langauge"]
        



        

