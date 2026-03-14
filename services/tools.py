def get_weather(city: str) -> str:
    # Answer simulation
    weather_data = {
        "Kyiv": "Rainy, 12°C",
        "London": "Cloudy, 15°C",
        "Lviv": "Sunny, 18°C"
    }
    return weather_data.get(city, "Unknown city")


def search_documents(query: str) -> str:
    docs = {
        "return policy": "Items can be returned within 30 days with receipt.",
        "shipping": "Free shipping on orders over $50. Standard delivery 3-5 days.",
        "warranty": "All products have 1 year manufacturer warranty."
    }
    for key, value in docs.items():
        if key in query.lower():
            return value
    return "No relevant documents found."


def create_ticket(issue: str, priority: str) -> str:
    ticket_id = f"TKT-{hash(issue) % 10000:04d}"
    return f"Ticket {ticket_id} created. Issue: {issue}. Priority: {priority}"

# Tools description for Claude
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name"
                }
            },
            "required": ["city"]
        }
    },
    {
        "name": "search_documents",
        "description": "Search company knowledge base for policies, shipping info, warranty details and other business information",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "document type"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "create_ticket",
        "description": "Ticket creating",
        "input_schema": {
            "type": "object",
            "properties": {
                "issue": {
                    "type": "string",
                    "description": "The ticket receiving reason"
                },
                "priority": {
                    "type": "string",
                    "description": "The ticket priority"
                }
            },
            "required": ["issue", "priority"]
        }
    }
]

