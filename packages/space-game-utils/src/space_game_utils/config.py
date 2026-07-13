_assets_path = None


def configure(assets_path):
    """Muss einmalig aufgerufen werden, bevor draw_hud() das erste Mal verwendet wird."""
    global _assets_path
    _assets_path = assets_path


def get_assets_path():
    if _assets_path is None:
        raise RuntimeError(
            "space_game_utils wurde noch nicht konfiguriert. Rufe zuerst "
            "space_game_utils.configure(settings.ASSETS_PATH) auf."
        )
    return _assets_path
