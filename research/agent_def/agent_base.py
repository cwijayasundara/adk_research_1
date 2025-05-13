from google.adk.agents import Agent
from google.genai import types
from dotenv import load_dotenv

def init_agent(model_name: str,
               agent_name: str = "agent_base",
               agent_description: str = "A default agent",
               instruction_prompt: str = "You are a helpful assistant.",
               content_config: types.GenerateContentConfig = types.GenerateContentConfig(temperature=0.2),
               tools: list = None
               ) -> Agent:
    """
    Initialize the agent with the specified model name.
    Args:
        model_name (str): The name of the model to be used.
        agent_name (str): The name of the agent.
        agent_description (str): A brief description of the agent's purpose.
        instruction_prompt (str): The instruction prompt for the agent.
    Returns:
        Agent: An instance of the agent initialized with the specified model.
    """

    return Agent(
        model=model_name,
        name=agent_name,
        description=agent_description,
        instruction=instruction_prompt,
        generate_content_config=content_config,
        tools=tools,
    )
