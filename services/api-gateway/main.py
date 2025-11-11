from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routes import servers, templates
from services import server_manager

app = FastAPI(
    title="Game Server API Gateway",
    version="1.0.0",
    description="Central API that routes requests to the appropriate game server microservices."
)

templates_dir = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    servers = server_manager.list_servers()
    return templates_dir.TemplateResponse("dashboard.html", {"request": request, "servers": servers})

# Include routers for different services
app.include_router(servers.router, prefix="/servers", tags=["Servers"])
app.include_router(templates.router, prefix="/templates", tags=["Templates"])
