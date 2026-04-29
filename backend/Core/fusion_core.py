# ==============================================================================
# PROPRIETARY AND CONFIDENTIAL
# OmniScan-XR System - Copyright (c) 2026 Serob Cholakyan
# ==============================================================================

import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from security import verify_operation_permit
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Scripts.nasa_fetcher import NasaEarthData
from Analysis.material_density import SpectralAnalyzer

load_dotenv()
app = Flask(__name__)
CORS(app)

PERMIT_STATUS = verify_operation_permit()
nasa_client = NasaEarthData()
analyzer = SpectralAnalyzer()

@app.route('/relay/lidar', methods=['POST'])
def process_spatial_data():
    if PERMIT_STATUS != "FULL":
        return jsonify({"error": "Unauthorized. Field operations require a valid permit."}), 403

    data = request.json
    vertices = data.get('vertices', [])
    print(f"📡 Cloud Core: Received {len(vertices)} spatial points.")

    nasa_data = nasa_client.fetch_emit_data(34.0, -118.0)

    return jsonify({
        "status": "processed",
        "nasa_sync": nasa_data['status'],
        "detections": [
            {"type": "Gold (Alunite Halo)", "probability": 0.89, "coords": {"x": 1.2, "y": -0.5, "z": 3.4}}
        ]
    })

if __name__ == "__main__":
    print("🚀 ort Cloud Server Initializing...")
    app.run(host='0.0.0.0', port=5001)
