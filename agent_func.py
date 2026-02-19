from google.adk import agents


def calculate_efficiency(output: int, input_power: int):
    """Calculates machine efficiency percentage."""
    return f"Efficiency is {(output/input_power)*100}%"

func_agent = agents.LlmAgent(
    name="Function_Agent",
    #model="gemini-2.0-flash",
    model="gemini-1.5-flash-latest",
    tools=[calculate_efficiency]
)