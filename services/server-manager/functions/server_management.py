import subprocess
import os

SERVERS_ROOT = "/servers"

def run_compose_command(server_name: str, command: str) -> dict:
    server_path = os.path.join(SERVERS_ROOT, server_name)
    if not os.path.exists(os.path.join(server_path, "docker-compose.yml")):
        return {"status": "error", "message": f"No docker-compose.yml found in {server_path}"}

    try:
        result = subprocess.run(
            ["docker", "compose", "-f", f"{server_path}/docker-compose.yml", command, "-d"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.stderr}
    
def list_servers() -> list:
    servers = []
    for name in os.listdir(SERVERS_ROOT):
        path = os.path.join(SERVERS_ROOT, name)
        if os.path.isdir(path):
            servers.append({"name": name, "path": path})
    return servers

def start_server(server_name: str) -> dict:
    return run_compose_command(server_name, "up")

def stop_server(server_name: str) -> dict:
    return run_compose_command(server_name, "down")

def restart_server(server_name: str) -> dict:
    stop_result = stop_server(server_name)
    if stop_result["status"] == "error":
        return stop_result
    return start_server(server_name)
