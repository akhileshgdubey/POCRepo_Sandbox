from google.adk import agents

search_agent = agents.LlmAgent(
    name="Search_Agent",
    #model="gemini-2.0-flash",
    model="gemini-1.5-flash-latest",
    instruction="You are a technical specialist. Answer questions based on manufacturing manuals."
)