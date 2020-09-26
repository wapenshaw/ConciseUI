"""
This script copies the mod from the project directory to the steam directory
for testing purposes.
"""

import shutil
from pathlib import Path

from build import build

# Paths
PATH_PROJECT = Path(__file__).parents[1]
PATH_MOD     = Path(PATH_PROJECT, 'mod')

# ! This is the path on my computer, if you want to try this script,
#   please change it to where you installed the steam.
PATH_STEAM = Path(r"E:\\Documents\\My Games\\Sid Meier's Civilization VI\\Mods\\ConciseUI")


def copy_():
    try:
        shutil.copytree(PATH_MOD, PATH_STEAM, dirs_exist_ok=True)
    except Exception as e:
        err_name = type(e).__name__
        print(f'[×] copy failed\n    > {err_name}: {e.args}')
    else:
        print('[√] copy complete')


if __name__ == "__main__":
    build()
    copy_()
