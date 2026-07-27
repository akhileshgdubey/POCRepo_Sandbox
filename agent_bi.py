from google.adk.agents import LlmAgent
from knowledge_graph.kg_tool import search_business_context
from analytics_tools.sql_generator import generate_sql
from analytics_tools.bigquery_tool import run_business_query


business_insight_agent = LlmAgent(
    name="Business_Insight_Agent",
    model="gemini-2.5-flash-lite",
    #model="gemini-2.5-flash",
    instruction="""

    You are a Business Insight Agent.

    For business analytics questions:

    1. First use search_business_context tool.
    2. Use the knowledge graph information to understand:
    - business definition
    - metric
    - tables
    - relationships

    3. Then use generate_sql tool to create SQL.

    4. Then use run_business_query tool to execute SQL.

    5. Return the final answer to the user.

    Do not answer from assumptions.
    Always use knowledge graph context first.

    """,

    tools=[
    search_business_context,
    generate_sql,
    run_business_query
    ]
)