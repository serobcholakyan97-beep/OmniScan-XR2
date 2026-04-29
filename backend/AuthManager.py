import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# 1. Load the secrets from your local .env file
load_dotenv()

class AuthManager:
    def __init__(self):
        # Fetching credentials from the .env file we created in the project folder
        self.nasa_user = os.getenv("NASA_USER")
        self.nasa_pass = os.getenv("NASA_PASS")
        self.nasa_token_url = "https://urs.earthdata.nasa.gov/api/users/token"
        
        # Starlink / SpaceX auth (if required by your specific gateway)
        self.starlink_key = os.getenv("SPACEX_TOKEN")

    def get_nasa_session(self):
        """
        Creates a persistent session with NASA Earthdata.
        This allows you to download hyperspectral mineral maps for Gold/Diamonds.
        """
        if not self.nasa_user or not self.nasa_pass:
            print("ERROR: NASA Credentials missing from .env file.")
            return None

        session = requests.Session()
        session.auth = (self.nasa_user, self.nasa_pass)
        
        try:
            # Test the connection to ensure the Earthdata Login is valid
            response = session.get("https://urs.earthdata.nasa.gov/profile")
            if response.status_code == 200:
                print("NASA Authentication: SUCCESS")
                return session
            else:
                print(f"NASA Authentication: FAILED (Status: {response.status_code})")
                return None
        except Exception as e:
            print(f"Connection Error: {e}")
            return None

    def verify_satellite_link(self):
        """
        Checks if the iPhone is successfully routed through the SpaceX Starlink gateway.
        """
        try:
            # Pinging the standard Starlink local gateway
            check = requests.get("http://192.168.100.1", timeout=2)
            if check.status_code == 200:
                return True
        except:
            return False
        return False

# Example usage for testing inside a-Shell:
if __name__ == "__main__":
    auth = AuthManager()
    nasa_session = auth.get_nasa_session()
    
    if auth.verify_satellite_link():
        print("Network: Connected to SpaceX Starlink")
    else:
        print("Network: Standard Cellular/WiFi")
