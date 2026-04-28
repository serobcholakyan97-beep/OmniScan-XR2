# ==============================================================================

# PROPRIETARY AND CONFIDENTIAL

# OmniScan-XR System - Copyright (c) 2026 Serob Cholakyan

# This code is protected under the OmniScan-XR Proprietary License.

# Commercial use or unauthorized field mining operations are strictly prohibited.

# ==============================================================================



import os

from flask import Flask, request, jsonify

from flask_cors import CORS



app = Flask(__name__)

CORS(app) # Allows the Android app to connect to the Cloud Terminal



@app.route('/relay/lidar', methods=['POST'])

def receive_spatial_data():

    data = request.json

    # Process Pixel 9a ARCore data in the Cloud

    print(f"Cloud Core: Received {len(data.get('vertices', []))} points from Pixel 9a")

    return jsonify({"status": "processed", "location": "GitHub-Cloud-Runner"})



if __name__ == "__main__":

    # GitHub Codespaces usually uses port 5001 or 8080

    app.run(host='0.0.0.0', port=5001)





Updated Android Bridge: CloudBridge.kt



package com.omniscan.xr



class CloudBridge {

    // Replace this with your actual GitHub Codespace Forwarding URL

    private val cloudUrl = "https://your-codespace-name-5001.app.github.dev/relay/lidar"



    // The rest of your transmit logic remains the same as our previous Kotlin bridge

}
