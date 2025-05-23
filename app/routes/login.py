from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.post("/login", response_class=HTMLResponse)
async def handle_login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "password":
        return f"<h2>Welcome, {username}!</h2>"
    return "<h2>Invalid credentials</h2>"
