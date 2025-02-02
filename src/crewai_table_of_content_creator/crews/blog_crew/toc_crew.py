from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TocCrew:
    """A crew that writes a blog Table of Contents about a given topic.""" 
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def toc_writer(self)-> Agent:
        return Agent(
            config = self.agents_config["toc_writer"]
        )
    @task
    def write_toc(self) -> Task:
        return Task(
            config = self.tasks_config['write_toc']
        )
    @crew
    def crew(self) -> Crew:
        return Crew(
                agent=self.agent,
                task=self.task,
                process=Process.sequential,
                verbos = True,
        )