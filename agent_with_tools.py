import os

from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService
from math_agent.agent import agent_math
from dotenv import load_dotenv
from agent_util import send_query_to_agent

load_dotenv()

MODEL = os.getenv("GOOGLE_MODEL")

AGENT_APP_NAME = 'single_agent'

session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()

if __name__ == '__main__':

    queries = [
        "Multiply 1 and 10",
        "Add 123 and 3 and 4",
        "Multiply the numbers between 1 and 10",
    ]

    for query in queries:
        send_query_to_agent(agent_math, query, session_service, artifact_service, AGENT_APP_NAME)
