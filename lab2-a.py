import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
#from agents import Agent, Runner
import agents

import asyncio 
import nest_asyncio
nest_asyncio.apply()

# Load environment variables
dotenv_path = os.path.join('../', 'config', '.env')
load_dotenv(dotenv_path)
api_key = os.getenv('OPENAI_API_KEY_TEG')
os.environ["OPENAI_API_KEY"] = api_key  
agents.set_default_openai_key(api_key, True)


agent = agents.Agent(name="Assistant", instructions="You are a helpful assistant")
result = await agents.Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)