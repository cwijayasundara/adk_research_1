from google.genai import types
import time
from google.adk.runners import Runner

def send_query_to_agent(agent, query, session_service, artifact_service, AGENT_APP_NAME):
    """Sends a query to the specified agent and prints the response.

    Args:
        agent: The agent to send the query to.
        query: The query to send to the agent.
        session_service: The session service to use.
        artifact_service: The artifact service to use.
        AGENT_APP_NAME: The name of the agent app.

    Returns:
        A tuple containing the elapsed time (in milliseconds) and the final response from the agent.
    """

    session = session_service.create_session(app_name=AGENT_APP_NAME,
                                             user_id='user',)
    
    print('\nUser Query: ', query)
    content = types.Content(role='user', parts=[types.Part(text=query)])

    # Start a timer to measure the response time
    start_time = time.time()

    runner = Runner(app_name=AGENT_APP_NAME, 
                    agent=agent, 
                    artifact_service=artifact_service, 
                    session_service=session_service)

    events = runner.run(user_id='user', session_id=session.id, new_message=content)

    final_response = None
    elapsed_time_ms = 0.0

    # Loop through the events returned by the runner
    for _, event in enumerate(events):

        is_final_response = event.is_final_response()

        if not event.content:
             continue

        if is_final_response:
            end_time = time.time()
            elapsed_time_ms = round((end_time - start_time) * 1000, 3)

            print("-----------------------------")
            print('>>> Inside final response <<<')
            print("-----------------------------")
            final_response = event.content.parts[0].text # Get the final response from the agent
            print(f'Agent: {event.author}')
            print(f'Response time: {elapsed_time_ms} ms\n')
            print(f'Final Response:\n{final_response}')
            print("----------------------------------------------------------\n")

    return elapsed_time_ms, final_response