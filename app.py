from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent


app = FastAPI()


class AgentRequest(BaseModel):
    request: str


@app.post("/agent")
def execute_agent(data: AgentRequest):

    result = run_agent(data.request)

    return {
        "status": "success",
        "message": "Agent completed execution",
        "plan": result["plan"],
        "generated_document": result["document"],
        "content": result["content"]
    }