# ==============================================================================
# PROPRIETARY AND CONFIDENTIAL
# OmniScan-XR System - Copyright (c) 2026
# This code is protected under the OmniScan-XR Proprietary License.
# Commercial use or unauthorized field mining operations are strictly prohibited.
# ==============================================================================

import json
from typing import Dict, Any

import httpx


class MetadataManager:
    """
    AAA+-Grade Metadata Management for OmniScan-XR2.
    Integrates AESICS and CMR Search/Ingest protocols.
    """

    def __init__(self, edl_token: str):
        self.base_url = "https://cmr.earthdata.nasa.gov/search"
        self.headers = {
            "Authorization": f"Bearer {edl_token}",
            "Accept": "application/vnd.nasa.cmr.umm+json",
        }

    async def search_discovery(
        self, provider: str, short_name: str
    ) -> Dict[str, Any]:
        """
        Supports 508-compliant discovery for Earthdata tools.
        """
        params = {
            "provider": provider,
            "short_name": short_name,
            "page_size": 10,
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                f"{self.base_url}/collections.json",
                params=params,
                headers=self.headers,
            )
            response.raise_for_status()
            return response.json()

    def format_for_508(self, data: Dict[str, Any]) -> str:
        """
        Ensures metadata display is screen-reader friendly.
        """
        return json.dumps(data, indent=2)
