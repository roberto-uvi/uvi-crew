import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
import logging


# Configure logging to see debug information
logging.basicConfig(level=logging.DEBUG)

# Ensure the required environment variables are loaded
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

# Define Agents
researcher = Agent(
    role='Researcher',
    goal='Research AI Insights',
    backstory='You are an AI Research Assistant',
    verbose=True,
    allow_delegation=False,
    max_iterations=10,  # Adjust the iteration limit as needed
    max_time=1200 # Adjust the time limit in seconds (e.g., 5 minutes)
)

writer = Agent(
    role='Writer',
    goal='Write compelling and engaging blog post about AI Trends and Insights',
    backstory='You are an AI blog post writer who specializes on AI topics',
    verbose=True,
    allow_delegation=False,
    max_iterations=10,  # Adjust the iteration limit as needed
    max_time=1200 # Adjust the time limit in seconds (e.g., 5 minutes)
)

# Define Tasks
task1 = Task(
    description='Research AI Trends in Natural Language Processing (NLP)',
    expected_output='A report detailing the 5 latest NLP trends',
    agent=researcher
)

task2 = Task(
    description='Research AI Trends in Computer Vision',
    expected_output='A report detailing the 5 latest Computer Vision trends',
    agent=researcher
)

task3 = Task(
    description='Write a compelling blog post integrating NLP and Computer Vision trends',
    expected_output='A 750 word or more blog post ready for publishing',
    agent=writer
)

# Create Crew with defined agents and tasks
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2, task3],
    verbose=True,
    process=Process.sequential
)

# Kickoff the Crew's workflow
result = crew.kickoff()

# Print the result
print(result)