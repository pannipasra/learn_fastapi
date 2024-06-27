from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["users"])
async def welcome_message_admin():
    return "Hi admin <3"