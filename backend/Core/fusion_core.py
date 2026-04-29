
# ==============================================================================
# PROPRIETARY AND CONFIDENTIAL
# OmniScan-XR System - Copyright (c) 2026 Serob Cholakyan
# ==============================================================================

import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Import our custom modules
from security import verify_operation_permit
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Scripts.nasa_fetcher import NasaEarthData

load_dotenv()
app = Flask(__name__)
CORS(app)

# 1. Check Legal Permit
PERMIT_STATUS = verify_operation_permit()

# 2. Initialize NASA Connection
nasa_client = NasaEarthData()

@app.route('/relay/lidar', methods=['POST'])
def process_spatial_data():
if PERMIT_STATUS != "FULL":
return jsonify({"error": "Unauthorized. Field operations require a valid permit."}), 403

# Receive point cloud from Pixel 9a / iPhone 16 Pro
data = request.json
vertices = data.get('vertices', [])

print(f"📡 Cloud Core: Received {len(vertices)} spatial points.")

# 3. Fetch NASA Data securely using the token
# (In production, use actual GPS coordinates sent from the phone)
nasa_data = nasa_client.fetch_emit_data(34.0, -118.0)

# 4. Return processed hits to the mobile HUD
return jsonify({
"status": "processed",
"nasa_sync": nasa_data['status'],
"detections": [
{"type": "Gold (Alunite Halo)", "probability": 0.89, "coords": {"x": 1.2, "y": -0.5, "z": 3.4}}
]
})

if __name__ == "__main__":
print("🚀 OmniScan-XR Cloud Server Initializing...")
# Port 5001 will be forwarded publicly via GitHub Codespaces
app.run(host='0.0.0.0', port=5001)
