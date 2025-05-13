from dotenv import load_dotenv
import os
from agent_def.agent_base import init_agent
from google.adk.tools import google_search

load_dotenv()

MODEL= os.getenv("GOOGLE_MODEL")
AGENT_NAME = os.getenv("SEARCH_AGENT_NAME")
AGENT_DESCRIPTION = os.getenv("SEARCH_AGENT_DESCRIPTION")
AGENT_INSTRUCTION_PROMPT = os.getenv("SEARCH_AGENT_PROMPT")

search_agent = init_agent(
    model_name=MODEL,
    agent_name=AGENT_NAME,
    agent_description=AGENT_DESCRIPTION,
    instruction_prompt=AGENT_INSTRUCTION_PROMPT,
    content_config=None,
    tools=[
        google_search
    ]
)