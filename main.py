from fastapi import FastAPI, HTTPException
import anthropic

from services.agent import run_agent
from schemas import AgentRequest, AgentResponse

app = FastAPI()

@app.post("/agent", response_model=AgentResponse)
async def run_agent_endp(request: AgentRequest):
    response = await run_agent(user_message=request.message)
    if not response:
        raise HTTPException(
            status_code=404,
            detail="Response not found"
        )
    return AgentResponse(answer=response)