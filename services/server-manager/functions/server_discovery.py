import random

import random

def list_servers():
    servers = ["minecraft", "csgo", "ark"]
    result = []

    for srv in servers:
        status = random.choice(["running", "stopped"])
        max_players = random.choice([10, 20, 50, 70])
        players = 0 if status == "stopped" else random.randint(1, max_players)

        cpu_limit = random.choice([1, 2, 4])  # em núcleos
        ram_limit = random.choice([2048, 4096, 8192])  # em MB

        cpu_usage = 0 if status == "stopped" else round(random.uniform(5, 85), 1)  # em %
        ram_usage = 0 if status == "stopped" else random.randint(512, ram_limit)

        uptime = 0 if status == "stopped" else random.randint(10, 720)  # minutos

        result.append({
            "name": f"{srv.capitalize()} Server",
            "path": f"/servers/{srv}",
            "type": srv,
            "status": status,
            "players": players,
            "max_players": max_players,
            "cpu_limit": cpu_limit,
            "cpu_usage": cpu_usage,
            "ram_limit": ram_limit,
            "ram_usage": ram_usage,
            "uptime_minutes": uptime
        })

    return result
