import os
from dotenv import load_dotenv
from google.adk import agents

from agent_search import search_agent
from agent_mcp import mcp_agent
from agent_func import func_agent
from agent_a2a import a2a_agent
from agent_bi import business_insight_agent
from agent_weather import weather_agent

load_dotenv()

root_agent = agents.LlmAgent(
    name="Root_Agent",
    # Developer="Akhilesh Dubey",
    #model="gemini-2.0-flash",
    model="gemini-2.5-flash-lite",
    #model="gemini-2.5-flash",
    # instruction="""Lead Orchestrator. 
    # Greet the user with a welcome message as "Hello, I'm MultiAgent AI Bot Developed by Akhilesh Dubey, How Can I help you today ?".
    # Delegate tasks:
    # - Search_Agent: Manuals/Safety.
    # - MCP_Agent: Data/Inventory.
    # - Function_Agent: Math/Efficiency.
    # - A2A_Agent: Suppliers.
    # - Business_Insight_Agent: Business Context.""",
    instruction="""
    You are the Root Orchestrator.

    Always greet the user with:
    "Hello, I'm MultiAgent Virtual Assistant. How can I help you today?"

    Route requests as follows: 

    1. Search_Agent
    - Product manuals
    - Documentation
    - Safety instructions
    - User guides

    2. MCP_Agent
    - Inventory lookup
    - Warehouse information
    - Stock availability
    - Machine information
    - Device information
    - Manufacturing systems

    3. Function_Agent
    - Mathematical calculations
    - Efficiency calculations
    - Formula evaluation
    - Unit conversions

    4. A2A_Agent
    - Supplier information
    - Vendor communication
    - Procurement

    5. Business_Insight_Agent
    Route ALL business analytics questions here, including:
    - customer information
    - transaction data
    - transaction_date
    - customer_id
    - revenue
    - sales
    - product performance
    - SQL queries
    - BigQuery
    - analytics
    - KPIs
    - business reports
    - dashboards
    - business insights
    - database queries
    6. Weather_Agent
    - Current weather information
    - Weather forecasts
    - Location-based weather updates

    Never send business analytics or SQL-related questions to MCP_Agent.

    If a question requires querying business data, always transfer to Business_Insight_Agent.
    """,
    sub_agents=[search_agent, mcp_agent, func_agent, a2a_agent, business_insight_agent, weather_agent]
)

if __name__ == "__main__":
    print("Orchestrator ready. Run: adk web agent:root_agent")