from typing import TypedDict
from pydantic import BaseModel,Field

class BlogModel(BaseModel):
    title:str=Field(description="The title of the blog post")
    content:str=Field(description="The main content of the blog post")

class BlogState(TypedDict):
    topic:str
    blog:BlogModel
    current_langauge:str

