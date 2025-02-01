from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class BlogCrew:
    """A crew that writes a blog post about a given topic."""
    agents_config = '/config/agents.yaml'
    tasks_config = '/config/tasks.yaml'

    pass
@CrewBase
class TocCrew:
    """A crew that writes a blog Table of Contents about a given topic.""" 
    agents_config = '/config/agents.yaml'
    tasks_config = '/config/tasks.yaml'
    pass