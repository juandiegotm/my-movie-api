from utils.jwt_manager import create_token
from main import app
from schemas.user import User
from fastapi.responses import JSONResponse

@app.post('/login', tags=['auth'], response_model=User)
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)