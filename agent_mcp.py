from google.adk import agents

# --- Mock Databases ---
INVENTORY_DB = {"motor_x": 10, "sensor_y": 55}
CALENDAR_DB = [] # Simulating calendar

# --- MCP Tools ---

def send_notification_email(recipient: str, subject: str, body: str):
    """MCP Action: Sends an automated email alert to a department head."""
    # In a real app, use an SMTP or SendGrid API here
    return f"EMAIL SUCCESS: Sent to {recipient} with subject: '{subject}'."

def schedule_maintenance_appointment(date: str, time: str, machine_id: str):
    """MCP Action: Book a slot in the technician's calendar for repairs."""
    appointment = {"date": date, "time": time, "machine": machine_id}
    CALENDAR_DB.append(appointment)
    return f"CALENDAR SUCCESS: Appointment confirmed for {machine_id} on {date} at {time}."

def get_warehouse_stock(item_id: str):
    """MCP Resource: Fetches real-time stock from the database."""
    stock = INVENTORY_DB.get(item_id.lower(), "Unknown")
    return f"STOCK REPORT: {item_id} has {stock} units available."

# --- MCP Agent ---

mcp_agent = agents.LlmAgent(
    name="MCP_Agent",
    #model="gemini-2.0-flash", 
    model="gemini-2.5-flash-lite",
    instruction="""You are an MCP Action Agent. You bridge the gap between data and action:
    1. If stock is low, offer to send an email to procurement using send_notification_email.
    2. If a machine needs repair, offer to schedule an appointment using schedule_maintenance_appointment.
    3. Always fetch data first using get_warehouse_stock before suggesting actions.""",
    tools=[send_notification_email, schedule_maintenance_appointment, get_warehouse_stock]
)