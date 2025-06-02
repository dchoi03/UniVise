from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.openai_agent import get_recommendation

router = APIRouter()


class promtRequest(BaseModel):
    prompt: str


@router.post("/recommend")
async def recommend(request: promtRequest):
    try:
        response = await get_recommendation(request.prompt)
        return {"recommendation": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
