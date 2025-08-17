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
        

