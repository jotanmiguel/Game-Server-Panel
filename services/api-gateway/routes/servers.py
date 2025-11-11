from fastapi import APIRouter, Path
from services import server_manager_client

router = APIRouter()

@router.get("/")
def get_servers():
    return server_manager_client.list_servers()

@router.post("/{name}/start")
def start(name: str = Path(...)):
    return server_manager_client.start_server(name)
