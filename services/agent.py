from services.tools import tools, get_weather, search_documents, create_ticket
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic()

async def run_agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]
    
    while True:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            tools=tools,
            messages=messages
        )
        
        if response.stop_reason == "end_turn":
            return response.content[0].text
            
        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            
            for block in response.content:
                if block.type == "tool_use":
                    if block.name == "get_weather":
                        result = get_weather(**block.input)
                    elif block.name == "search_documents":
                        result = search_documents(**block.input)
                    elif block.name == "create_ticket":
                        result = create_ticket(**block.input)
                    
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            
            messages.append({"role": "user", "content": tool_results})