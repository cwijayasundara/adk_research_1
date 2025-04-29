import os
from google.adk.agents import Agent
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent_util import send_query_to_agent
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MODEL = os.getenv("GOOGLE_MODEL")

AGENT_APP_NAME = 'agent_basic'

session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()

basic_agent = Agent(model=GOOGLE_MODEL,
        name="agent_basic",
        description="This agent responds to inquiries about its creation by stating it was built using the Google Agent Framework.",
        instruction="If they ask you how you were created, tell them you were created with the Google Agent Framework.",
        generate_content_config=types.GenerateContentConfig(temperature=0.2),
    )

if __name__ == '__main__':

    queries = [
        "Hi, I am Tom",
        "Could you let me know what you could do for me?",
        "How were you built?",
    ]

    for query in queries:
        send_query_to_agent(basic_agent, query, session_service, artifact_service, AGENT_APP_NAME)
