import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from agents import Agent, Runner
import agents

import asyncio 
import nest_asyncio
nest_asyncio.apply()

tools = [{
    "type": "function",
    "function": {
        "name": "calculate",
        "description": "Double the number.",
        "parameters": {
            "type": "object",
            "properties": {
                "number": {
                    "type": "float",
                    "description": "Any number."
                }
            },
            "required": [
                "number"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]

async def calculate(number: float):
    print("Doubling the number:{number}")
    double_number =  number *2
    return f"The text has {double_number} words"

async def main():

    # Load environment variables
    dotenv_path = os.path.join('../', 'config', '.env')
    load_dotenv(dotenv_path)
    api_key = os.getenv('OPENAI_API_KEY_TEG')
    os.environ["OPENAI_API_KEY"] = api_key  
    agents.set_default_openai_key(api_key, True)
    agent = Agent(name="Assistant", 
                  instructions="You are a helpful assistant",
                  model = "gpt-4o-mini",
                  tools=tools
                  )
    #result = await agents.Runner.run_sync(agent, "Write a haiku about recursion in programming.")
    result = Runner.run_sync(agent, "how much is 2*2?")
    #result = await Runner.run(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())