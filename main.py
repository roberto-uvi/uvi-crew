import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

info_agent = Agent(
    role="Information Agent",
    goal="Give Compelling information about certain topic",
    backstory="""
        You love to know information. People love and hate you for it. 
        You win most of the quizzes at your local pub.
    """
)

task1 = Task(
    description="Tell me all about the Beaches Resorts.",
    expected_output="Give me a quick summary and also give me 7 bullet points describing it.",
    agent=info_agent
)

crew = Crew(
    agents=[info_agent],
    tasks=[task1],
    verbose=True
)

result = crew.kickoff()

print("############")
print(result)