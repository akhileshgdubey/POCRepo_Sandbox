from google.adk import agents


def check_supplier_delivery():
    """Simulates A2A communication with a supplier's agent."""
    return "Supplier Agent confirms: Delivery is scheduled for Friday."

a2a_agent = agents.LlmAgent(
    name="A2A_Agent",
    #model="gemini-2.0-flash",
    model="gemini-1.5-flash-latest",
    tools=[check_supplier_delivery]
)