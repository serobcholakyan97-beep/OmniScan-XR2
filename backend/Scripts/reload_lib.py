# ==============================================================================
# PROPRIETARY AND CONFIDENTIAL
# OmniScan-XR System - Copyright (c) 2026
# This code is protected under the OmniScan-XR Proprietary License.
# Commercial use or unauthorized field mining operations are strictly prohibited.
# ==============================================================================

import json
import os


def reload_spectral_config():
    """
    Reloads the spectral library JSON file from disk.

    Returns:
        dict | None: Parsed spectral library or None if file not found.
    """
    lib_path = "backend/Data/spectral_lib.json"

    if os.path.exists(lib_path):
        with open(lib_path, "r", encoding="utf-8") as f:
            new_config = json.load(f)

        print(
            f"📡 Cloud Core: Spectral Library Reloaded. "
            f"Tracking {len(new_config['minerals'])} minerals."
        )
        return new_config

    return None


if __name__ == "__main__":
    reload_spectral_config()
