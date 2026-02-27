import os
from dotenv import load_dotenv
from google.adk import agents

from agent_search import search_agent
from agent_mcp import mcp_agent
from agent_func import func_agent
from agent_a2a import a2a_agent

load_dotenv()

root_agent = agents.LlmAgent(
    name="Root_Agent",
    #Developer="Akhilesh Dubey",
    #model="gemini-2.0-flash",
    model="gemini-2.5-flash-lite",
    instruction="""Lead orchestrator. Delegate tasks:
    - Search_Agent: Manuals/Safety.
    - MCP_Agent: Data/Inventory.
    - Function_Agent: Math/Efficiency.
    - A2A_Agent: Suppliers.""",
    sub_agents=[search_agent, mcp_agent, func_agent, a2a_agent]
)

if __name__ == "__main__":
    print("Orchestrator ready. Run: adk web agent:root_agent")