from fastapi import APIRouter,Request
from app.config import VERIFY_TOKEN
from app.whatsapp import parse_incoming, send_reply
from app.ai import get_agent_reply

router = APIRouter()

@router.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params

    if params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params.get("hub.challenge"))

    return {"error" : "Invalid verify token"}
@router.post("/webhook")
async def any(request: Request):
    data = await request.json()
    sender,text = parse_incoming(data)
    reply = get_agent_reply(text)
    send_reply(sender,reply)
    return {"status": "ok"}