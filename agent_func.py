from google.adk import agents

# --- Factory Operational Tools ---

def calculate_oee(availability: float, performance: float, quality: float):
    """
    Calculates Overall Equipment Effectiveness (OEE).
    Industry standard for measuring manufacturing productivity.
    """
    oee = (availability * performance * quality) / 100
    status = "World Class" if oee >= 85 else "Needs Optimization"
    return f"ANALYSIS: OEE is {oee:.2f}%. Status: {status}."

def estimate_repair_roi(replacement_cost: float, repair_cost: float, extended_life_years: int):
    """
    Financial Tool: Determines if it's better to repair or replace a machine.
    """
    savings = replacement_cost - repair_cost
    annual_benefit = savings / extended_life_years
    return f"FINANCIAL: Repairing saves ${savings}. Annual value of repair: ${annual_benefit:.2f}/year."

def predict_failure_window(current_temp: float, vibration_level: float):
    """
    Predictive Maintenance: Analyzes sensor thresholds to predict downtime risk.
    """
    if current_temp > 85.0 or vibration_level > 7.5:
        return "CRITICAL: High risk of failure detected. Schedule maintenance within 24 hours."
    return "HEALTH: Machine parameters are within safe operational limits."

# --- Enhanced Function Agent ---

func_agent = agents.LlmAgent(
    name="Operations_Analyst",
    #model="gemini-2.0-flash", 
    model="gemini-2.5-flash-lite",
    instruction="""You are an Industrial Operations Analyst. 
    Your goal is to provide data-driven insights:
    1. Use 'calculate_oee' to report on line productivity.
    2. Use 'estimate_repair_roi' when users ask about costs vs. benefits of fixing equipment.
    3. Use 'predict_failure_window' to assess machine health.
    Always explain the 'Why' behind your calculations to the user.""",
    tools=[calculate_oee, estimate_repair_roi, predict_failure_window]
)