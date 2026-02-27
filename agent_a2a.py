from google.adk import agents

# --- Mock External Agent Responses ---
# In a real demo, these represent "handshakes" with another AI
def negotiate_price(item_name: str, quantity: int, target_price: float):
    """
    A2A Handshake: Contacts the Vendor Agent to negotiate a bulk discount.
    """
    market_price = 50.0  # Simulating vendor's starting price
    
    if target_price >= market_price:
        return f"A2A SUCCESS: Vendor_Agent accepted ${target_price}. Order Reserved."
    else:
        return f"A2A COUNTER-OFFER: Vendor_Agent rejected ${target_price}. Lowest possible is $48.50."

def get_supplier_shipping_eta(order_id: str):
    """
    A2A Query: Pings the Logistics Agent for real-time fleet tracking.
    """
    return f"A2A LOGISTICS: Courier_Agent reports Order {order_id} is 15 miles away. ETA: 45 mins."

def check_external_availability(item_name: str):
    """
    A2A Inquiry: Checks the global supplier network for stock availability.
    """
    return f"A2A NETWORK: Global_Supplier_Agent confirms 500 units of {item_name} in the European Hub."

# --- Enhanced A2A Agent ---

a2a_agent = agents.LlmAgent(
    name="A2A_Agent",
    #model="gemini-2.0-flash",
    model="gemini-2.5-flash-lite",
    instruction="""You are an Autonomous Procurement Agent. 
    Your goal is to handle interactions with External AI Agents:
    1. Use 'negotiate_price' when the user wants a better deal or needs to buy parts.
    2. Use 'get_supplier_shipping_eta' to track existing vendor deliveries.
    3. Use 'check_external_availability' to see if parts exist outside our factory.
    Be professional and always report the 'Agent Handshake' status.""",
    tools=[negotiate_price, get_supplier_shipping_eta, check_external_availability]
)