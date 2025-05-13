import os
from search_agent.search_agent import search_agent
from calc_agent.calc_agent import math_agent
from util.agent_util import send_query_to_agent
from dotenv import load_dotenv

load_dotenv()

SEARCH_AGENT_NAME = 'basic_search_agent'
MATH_AGENT_NAME = 'basic_math_agent'

if __name__ == '__main__':

    search_queries = [
        "Whats the weather like today in London?",
        "Whats AdS/CFT?",
        "What is TIME?",
    ]

    for query in search_queries:
        send_query_to_agent(search_agent,
                            query,
                            SEARCH_AGENT_NAME)
    print("----------------------------------------------------------\n")
    math_queries = [
        "What is 2 + 2?",
        "What is 5 * 3?",
        "What is the square root of 16?",
        "What is 10 - 4?",
        "What is 8 / 2?"
    ]
    for query in math_queries:
        send_query_to_agent(math_agent,
                            query,
                            MATH_AGENT_NAME)

    print("----------------------------------------------------------\n")
    

