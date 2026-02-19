from google.adk import agents


def get_warehouse_stock(item_id: str):
    """Fetches real-time stock from the database (MCP simulation)."""
    return f"Item {item_id}: 120 units available in Sector-7."

mcp_agent = agents.LlmAgent(
    name="MCP_Agent",
    #model="gemini-2.0-flash",
    model="gemini-1.5-flash-latest",
    tools=[get_warehouse_stock]
)