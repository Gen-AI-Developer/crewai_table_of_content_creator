#!/usr/bin/env python
from random import randint

from crewai.flow import Flow, listen, start
from pydantic import BaseModel

from crewai_table_of_content_creator.crews.blog_crew.blog_crew import BlogCrew
from crewai_table_of_content_creator.crews.blog_crew.toc_crew import TocCrew

class BlogState(BaseModel):
    word_count: int =1000
    topic: str = "CrewAI"
    blog_post: str = ""

class TocState(BaseModel):
    table_of_contents: str = ""

class TOCFlow(Flow[TocState]):

    @start()
    def generate_toc(self): # -> TocState:
        result = (TocCrew().crew().kickoff(inputs={"table_of_contents": self.state.table_of_contents}))
        self.state.table_of_contents = result.raw

class BlogFlow(Flow[BlogState]):
    @start()
    def generate_blog_post(self): # -> BlogState:
        result = (BlogCrew().crew().kickoff(inputs={"word_count": self.state.word_count, "table_of_contents": TocState.table_of_contents, "topic": self.state.topic}))
        self.state.blog_post = result.raw
        
    @listen(generate_blog_post)
    def save_blog_post(self):
        print("Saving Blog")
        with open("blog.txt", "w") as f:
            f.write(self.state.blog)
    
def kickoff():
    toc_flow = TOCFlow()
    toc_flow.kickoff()
    blog_flow = BlogFlow()
    blog_flow.kickoff()


def plot():
    # blog_flow = BlogFlow()
    # blog_flow.plot()
    pass


if __name__ == "__main__":
    kickoff()
