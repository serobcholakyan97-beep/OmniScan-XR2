# ==============================================================================

# PROPRIETARY AND CONFIDENTIAL

# OmniScan-XR System - Copyright (c) 2026 Serob Cholakyan

# This code is protected under the OmniScan-XR Proprietary License.

# Commercial use or unauthorized field mining operations are strictly prohibited.

# ==============================================================================

import json
import numpy as np

class SpectralAnalyzer:
    def __init__(self, lib_path="../Data/spectral_lib.json"):
        with open(lib_path, 'r') as f:
            self.library = json.load(f)

    def analyze_tile(self, swir1_data, swir2_data, nir_data):
        """
        Processes arrays of spectral data to find target indices.
        Returns probability matrices.
        """
        # Calculate Gold Index (SWIR1 / SWIR2)
        # using numpy to handle potential divide-by-zero errors safely
        gold_index = np.divide(swir1_data, swir2_data, 
                               out=np.zeros_like(swir1_data), 
                               where=swir2_data!=0)
        
        # Determine hits based on thresholds in the library
        gold_threshold = self.library["minerals"]["24k_Gold_Alteration"]["absorption_depth_min"]
        
        # Creates a boolean mask where the index exceeds the threshold
        hotspots = gold_index > gold_threshold
        
        return hotspots
