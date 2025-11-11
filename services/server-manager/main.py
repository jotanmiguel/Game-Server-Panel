from fastapi import FastAPI
from services.server_management import server_management

app = FastAPI()

@app.get("/servers")
def list_servers():
    return server_management.list_servers()

@app.post("/servers/{server_name}/start")
def start(server_name: str):
    return server_management.start_server(server_name)

@app.post("/servers/{server_name}/stop")
def stop(server_name: str):
    return server_management.stop_server(server_name)

@app.post("/servers/{server_name}/restart")
def restart(server_name: str):
    return server_management.restart_server(server_name)
