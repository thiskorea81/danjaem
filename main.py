# main.py

from fastapi import FastAPI, Request
from routers.users import router as users_router
from routers.auth import router as auth_router
from database import engine
from models import Base

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.include_router(users_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

# 'frontend' 폴더 내의 정적 파일 제공
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# HTML 템플릿을 위한 설정
templates = Jinja2Templates(directory="frontend/html")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)