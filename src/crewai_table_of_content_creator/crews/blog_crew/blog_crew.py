from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class BlogCrew:
    """A crew that writes a blog post about a given Table of Contents."""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def blog_writer(self)-> Agent:
        return Agent(
            config = self.agents_config['blog_writer']
        )
    @task
    def write_blog_post(self) -> Task:
        return Task(
            config = self.tasks_config['write_blog_post'],
        )
    @crew
    def blog_crew(self) -> Crew:
        return Crew (
            agents=self.agents,
            tasks=self.tasks,
            process = Process.sequential,
            verbos= True,
            
        )

