# ### below is v2 model pydantic
# from typing import TypedDict
# from pydantic import BaseModel,Field

# class BlogModel(BaseModel):
#     title:str=Field(description="The title of the blog post")
#     content:str=Field(description="The main content of the blog post")

# class BlogState(TypedDict):
#     topic:str
#     blog:BlogModel
#     current_langauge:str

### PyDantic V1 Model
from typing import TypedDict
from pydantic.v1 import BaseModel, Field  # 👈 force v1

class BlogModel(BaseModel):
    title: str = Field(description="The title of the blog post")
    content: str = Field(description="The main content of the blog post")

class BlogState(TypedDict):
    topic: str
    blog: BlogModel
    current_langauge: str
