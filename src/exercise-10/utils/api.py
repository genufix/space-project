import httpx
from entity.player import Player


class Client:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def send_player_data(self, player: Player) -> httpx.Response:
        data = {
            "name": player.name,
            "time_lived": player.time_lived,
            "asteroids_destroyed": player.asteroids_destroyed,
        }
        response = httpx.post(f"{self.base_url}/score", json=data)
        return response

    def get_player_data(self, player) -> httpx.Response:
        response = httpx.get(f"{self.base_url}/score", params={"name": player.name})
        return response


api_client = Client("http://localhost:1234/xyz")
