import httpx
import pygame
import settings
import space_game_entities
import space_game_ui
import space_game_utils
from space_game_entities import Player, projectiles, Asteroid, asteroids
from space_game_physics import PhysicsWorld
from space_game_utils import load_background, get_device_id, ApiClient, draw_hud
from space_game_ui import Menu


pygame.init()
pygame.mixer.init()
space_game_entities.configure(settings.ASSETS_PATH)
space_game_ui.configure(settings.ASSETS_PATH)
space_game_utils.configure(settings.ASSETS_PATH)

# Create the window first, then load the icon from your assets folder
display_surface = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

icon_path = str(settings.ASSETS_PATH / "images" / "icons.png")
pygame.display.set_icon(pygame.image.load(icon_path))

pygame.display.set_caption("Space Shooter Game")

pygame.display.set_caption("Space Shooter Game")
clock = pygame.time.Clock()
delta_time = 0

asteroid_world = PhysicsWorld()
player_world = PhysicsWorld(damping=0.15)

background = load_background(
    settings.ASSETS_PATH / "images" / "background" / "starfield" / "tile_1.png"
)

menu = Menu(display_surface)
player_name = menu.start_screen(background=background)
if player_name is None:
    pygame.quit()
    raise SystemExit

game_music = pygame.mixer.Sound(
    settings.ASSETS_PATH / "music" / "synthwave" / "loop_7.mp3"
)
GAME_MUSIC_VOLUME = 0.5
game_music.set_volume(GAME_MUSIC_VOLUME)
game_music.play(loops=-1, fade_ms=1000)
alarm = pygame.mixer.Sound(settings.ASSETS_PATH / "sounds" / "alarm" / "loop_3.wav")
alarm.set_volume(0.3)
impact = pygame.mixer.Sound(settings.ASSETS_PATH / "sounds" / "impact" / "blast_1.wav")
impact.set_volume(0.5)
death_sound = pygame.mixer.Sound(
    settings.ASSETS_PATH / "sounds" / "impact" / "loose_1.wav"
)
death_sound.set_volume(0.2)

player = Player(
    (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2),
    physics_world=player_world,
)

game_start_time = pygame.time.get_ticks()

last_asteroid_spawn = 0
asteroid_cooldown = 1000  # in ms
api_client = ApiClient(settings.API_BASE_URL)
device_id = get_device_id(settings.ASSETS_PATH / ".." / "device_id.txt")
try:
    player_id = api_client.create_player(device_id, player_name)
except httpx.HTTPError:
    print("Konnte keine Verbindung zur API aufbauen. Der Score wird nicht gespeichert.")
    player_id = None
running = True
while running:
    # 1. Eingaben (Events) abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_music.set_volume(GAME_MUSIC_VOLUME * 0.2)
            pause_started = pygame.time.get_ticks()
            if not menu.pause_screen(background=display_surface.copy()):
                running = False
            game_music.set_volume(GAME_MUSIC_VOLUME)
            game_start_time += pygame.time.get_ticks() - pause_started
            clock.tick()  # Pause nicht in die nächste Delta Time einrechnen

    display_surface.blit(background)

    time_lived = (pygame.time.get_ticks() - game_start_time) / 1000

    asteroid_world.step(delta_time)
    player_world.step(delta_time)

    projectile_asteroid_collisions = pygame.sprite.groupcollide(
        projectiles, asteroids, True, True
    )
    for destroyed_asteroids in projectile_asteroid_collisions.values():
        player.asteroids_destroyed += len(destroyed_asteroids)
        impact.play()

    if pygame.sprite.spritecollide(player, asteroids, dokill=True):
        player.lives -= 1
        impact.play()
        if player.lives == 0:
            alarm.stop()
            game_music.stop()
            death_sound.play()

            if player_id is not None:
                try:
                    api_client.submit_score(
                        player_id, player.asteroids_destroyed, time_lived
                    )
                except httpx.HTTPError:
                    print("Score konnte nicht gesendet werden.")

            if menu.death_screen(
                player.asteroids_destroyed,
                time_lived,
                background=display_surface.copy(),
            ):
                for asteroid in asteroids.sprites():
                    asteroid.kill() 
                projectiles.empty()
                player_world.remove(player.physics_body)
                player = Player(
                    (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2),
                    physics_world=player_world,
                )
                game_start_time = pygame.time.get_ticks()
                last_asteroid_spawn = 0
                game_music.play(loops=-1, fade_ms=1000)
                clock.tick() 
            else:
                running = False
            continue
        elif player.lives == 1:
            alarm.play()

    projectiles.update(delta_time)
    asteroids.update(delta_time)
    player.update(delta_time)

    current_time = pygame.time.get_ticks()
    if current_time - last_asteroid_spawn >= asteroid_cooldown:
        Asteroid(physics_world=asteroid_world)
        last_asteroid_spawn = current_time

    projectiles.draw(display_surface)
    asteroids.draw(display_surface)
    display_surface.blit(player.image, player.rect)
    draw_hud(player.lives, player.asteroids_destroyed, time_lived)

    pygame.display.flip()

    delta_time = clock.tick(settings.FRAMERATE) / 1000  # ms -> Sekunden

pygame.quit()
