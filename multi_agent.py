import os
import time
from google.adk.agents import SequentialAgent
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService
from math_agent.agent import agent_math
from agent_grammar.agent import agent_grammar
from agent_summary.agent import agent_summary
from agent_util import send_query_to_agent
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("GOOGLE_MODEL")
AGENT_APP_NAME = 'multi_agent'

session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()

agent_teaching_assistant = SequentialAgent(
        name="agent_teaching_assistant",
        description="This agent acts as a friendly teaching assistant, checking the grammar of kids' questions, performing math calculations using corrected or original text (if grammatically correct), and providing results or grammar feedback in a friendly tone.",
        sub_agents=[agent_grammar, agent_math, agent_summary],
    )

if __name__ == '__main__':

    queries = [
       "Multiply 1 and 10",
       "Add 123 and 3 and 4",
       "Multiply the numbers between 1 and 10",
    ]

    for query in queries:
       send_query_to_agent(agent_math, query, session_service, artifact_service, AGENT_APP_NAME)
