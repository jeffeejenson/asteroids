GitHub Copilot Chat Assistant

# Asteroids

Asteroid game built with Pygame.

## About
A simple Asteroids-style arcade game implemented in Python using Pygame. Pilot a ship, avoid or destroy asteroids, and try to survive as long as possible.

## Requirements
- Python 3.8+ (use your preferred version)
- pygame

Install pygame:
pip install pygame

## Run (using venv)
From the repo root:

python3 -m venv .venv

source .venv/bin/activate  

uv run main.py

deactivate

Want me to commit this change to README.md in jeffeejenson/asteroids?

## Controls
- Arrow keys or WASD — move / rotate / thrust (typical controls)
- Space — shoot
- Esc / close window — quit



## Project structure (key files)
- main.py — game entry point
- player.py — player ship logic
- asteroid.py — asteroid behavior
- asteroidfield.py — manages asteroids
- shot.py — projectile handling
- circleshape.py — shape/collision helpers
- constants.py — configuration values
- logger.py — game logging
- game_events.jsonl — recorded events / logs
- pyproject.toml, .python-version, .gitignore


## Disclaimer

-This is primarily a practice project
