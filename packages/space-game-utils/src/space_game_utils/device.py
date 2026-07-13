import uuid
from os import PathLike
from pathlib import Path


def get_device_id(path: str | PathLike) -> str:
    """Liest die dauerhafte Geräte-ID aus `path` - oder erzeugt und speichert eine neue,
    falls die Datei noch nicht existiert (oder leer ist)."""
    path = Path(path).resolve()

    if path.exists():
        device_id = path.read_text().strip()
        if device_id:
            return device_id

    device_id = str(uuid.uuid4())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(device_id)
    return device_id
