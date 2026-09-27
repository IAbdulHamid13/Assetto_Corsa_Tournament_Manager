"""
WSGI config for Tournament_Manager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os
import configparser
from django.core.wsgi import get_wsgi_application
from pathlib import Path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tournament_manager.settings')

application = get_wsgi_application()

def populateCarsFromIni():
    from main.models import Car
    base_dir = Path(__file__).resolve().parent.parent
    ini_path = base_dir / 'main' / 'car_list' / 'car_list.ini'

    if not ini_path.exists():
        print(f"[WSGI STARTUP] INI FILE NOT FOUND AT {ini_path}")
        return

    config = configparser.ConfigParser()
    config.read(ini_path)

    for section in config.sections():
        # Assetto Corsa configuration sections start with CAR_
        if section.upper().startswith('CAR_'):
            model_name = config.get(section, 'MODEL', fallback='')
            skin_name = config.get(section, 'SKIN', fallback='')
            driver_name = config.get(section, 'DRIVERNAME', fallback='')
            team_name = config.get(section, 'TEAM', fallback='')
            guid_str = config.get(section, 'GUID', fallback='')
            
            spectator = config.getint(section, 'SPECTATOR_MODE', fallback=0)
            ballast_val = config.getint(section, 'BALLAST', fallback=0)
            restrictor_val = config.getint(section, 'RESTRICTOR', fallback=0)

            # Use update_or_create to prevent duplicate entries on server reload
            Car.objects.update_or_create(
                model=model_name,
                skin=skin_name,
                drivername=driver_name,
                defaults={
                    'spectator_mode': spectator,
                    'team': team_name,
                    'guid': guid_str,
                    'ballast': ballast_val,
                    'restrictor': restrictor_val,
                }
            )

    print(f"[WSGI Startup] Successfully updated car list from {ini_path}")

populateCarsFromIni()