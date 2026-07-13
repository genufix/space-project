import httpx


class ApiClient:
    """Kleiner HTTP-Client für die Score-API (siehe Aufgabe 9)."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_player(self, device_id: str, name: str) -> int:
        """Registriert den Spieler bei der API und gibt seine Spieler-ID zurück."""
        response = httpx.post(
            f"{self.base_url}/spieler",
            params={"device_id": device_id, "name": name},
        )
        response.raise_for_status()
        return response.json()["id"]

    def submit_score(
        self, player_id: int, asteroids_destroyed: int, time_lived: float
    ) -> None:
        """Meldet einen Score für die übergebene Spieler-ID an die API."""
        response = httpx.put(
            f"{self.base_url}/spieler/{player_id}/scores",
            params={
                "player_id": player_id,
                "asteroids_destroyed": asteroids_destroyed,
                "time_lived": time_lived,
            },
        )
        response.raise_for_status()
