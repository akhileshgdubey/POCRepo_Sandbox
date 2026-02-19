import os
from dotenv import load_dotenv
from google.adk import agents

# 1. Import your individual specialists from their files
from agent_search import search_agent
from agent_mcp import mcp_agent
from agent_func import func_agent
from agent_a2a import a2a_agent

# 2. Load your API Key from the .env file
load_dotenv()

# 3. Create the "Root Agent" (The Boss)
# This agent listens to the user and decides which specialist to call.

root_agent = agents.LlmAgent(
    name="PwC_Manufacturing_Chief",
    #model="gemini-2.0-flash",
    model="gemini-1.5-flash-latest",
    instruction="""You are the lead orchestrator. 
    Analyze the user's request and delegate tasks:
    - If they ask about manuals or technical docs, use Search_Agent.
    - If they ask about inventory or data, use MCP_Agent.
    - If they need math or machine efficiency, use Function_Agent.
    - If they ask about suppliers or external partners, use A2A_Agent.""",
    sub_agents=[search_agent, mcp_agent, func_agent, a2a_agent]
)

# 4. (Optional) Simple terminal test
if __name__ == "__main__":
    #print("Orchestrator is ready. Run 'adk web main:root_agent' to start the UI.")
    print("Orchestrator is ready. Run 'adk web main:agent'...")