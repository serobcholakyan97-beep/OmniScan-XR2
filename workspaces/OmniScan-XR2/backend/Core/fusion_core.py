from fastapi import FastAPI
# Import new services
from backend.Services.OmniScan_Metadata_Manager import MetadataManager
from backend.Services.MultiDAAC_Client import MultiDAACClient
from backend.Services.Sentinel_Compliance_Handler import SentinelHandler

app = FastAPI()

# Initialize the clients when the server starts
daac_client = MultiDAACClient()
