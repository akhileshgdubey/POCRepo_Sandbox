from google.adk import agents

# Local Knowledge Base
MANUALS = {
    "safety": "Standard Protocol: Wear high-vis gear and power down machines before inspection.",
    "repair": "Standard Protocol: Use a 10mm wrench for the motor housing bolts.",
}

def search_manuals(topic: str):
    """Retrieves specific data from the technical documentation library."""
    result = MANUALS.get(topic.lower(), "Topic not found in current manuals.")
    return f"Retrieved Content: {result}"

search_agent = agents.LlmAgent(
    name="Search_Agent",
    #model="gemini-2.0-flash",
    model="gemini-2.5-flash-lite",
    instruction="You are a knowledge expert. Use the search tool to verify procedures before answering.",
    tools=[search_manuals]
)