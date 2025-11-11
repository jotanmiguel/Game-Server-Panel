import httpx

BASE_URL = "http://server-manager:8081"

def list_servers():
    try:
        response = httpx.get(f"{BASE_URL}/servers")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def start_server(name: str):
    try:
        response = httpx.post(f"{BASE_URL}/servers/{name}/start")
        return response.json()
    except Exception as e:
        return {"error": str(e)}
