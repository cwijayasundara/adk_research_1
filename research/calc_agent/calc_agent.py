from tools.calc_tools import add, subtract, multiply, divide
from dotenv import load_dotenv
import os
from agent_def.agent_base import init_agent

load_dotenv()

MODEL= os.getenv("GOOGLE_MODEL")
AGENT_NAME = os.getenv("MATH_AGENT_NAME")
AGENT_DESCRIPTION = os.getenv("MATH_AGENT_DESCRIPTION")
AGENT_INSTRUCTION_PROMPT = os.getenv("MATH_AGENT_PROMPT")

math_agent = init_agent(
    model_name=MODEL,
    agent_name=AGENT_NAME,
    agent_description=AGENT_DESCRIPTION,
    instruction_prompt=AGENT_INSTRUCTION_PROMPT,
    content_config=None,
    tools=[
        add,
        subtract,
        multiply,
        divide
    ]
)