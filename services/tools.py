import chromadb

chroma = chromadb.PersistentClient(path="./chroma_db")
collection = chroma.get_or_create_collection("documents")

def get_weather(city: str) -> str:
    # Answer simulation
    weather_data = {
        "Kyiv": "Rainy, 12°C",
        "London": "Cloudy, 15°C",
        "Lviv": "Sunny, 18°C"
    }
    return weather_data.get(city, "Unknown city")


def search_documents(query: str) -> str:
    results = collection.query(
        query_texts=[query],
        n_results=2
    )
    docs = results["documents"][0]
    if not docs:
        return "No relevant document found"
    return "\n\n".join(docs)


def create_ticket(issue: str, priority: str) -> str:
    ticket_id = f"TKT-{hash(issue) % 10000:04d}"
    return f"Ticket {ticket_id} created. Issue: {issue}. Priority: {priority}"



def split_into_chunks(text: str, chunk_size: int = 200) -> list[str]:
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks


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
        "description": "Search through uploaded documents to find relevant information based on a query. Use this when the user asks about content from any document.",
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

