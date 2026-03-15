from fastapi import FastAPI, HTTPException
import anthropic

from services.agent import run_agent
from schemas import AgentRequest, AgentResponse
from services.tools import collection, split_into_chunks

app = FastAPI()


@app.post("/upload")
async def upload(doc_id: str, text: str):
    chunks = split_into_chunks(text)
    ids = [f"{doc_id}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"doc_id": doc_id} for _ in chunks]
    collection.add(documents=chunks, ids=ids, metadatas=metadatas)
    return {"chunks": len(chunks)}

@app.post("/agent", response_model=AgentResponse)
async def run_agent_endp(request: AgentRequest):
    response = await run_agent(user_message=request.message)
    if not response:
        raise HTTPException(
            status_code=404,
            detail="Response not found"
        )
    return AgentResponse(answer=response)