"""
Sentinel Compliance Handler.

Handles asynchronous communication with the Sentinel compliance service.
"""

import logging
from typing import Any, Dict, Optional

import httpx

logger = logging.getLogger(__name__)


class SentinelComplianceHandler:
    """Client for Sentinel compliance checks."""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        timeout_seconds: float = 10.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = httpx.Timeout(timeout_seconds)

    async def check_compliance(
        self,
        payload: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Send a compliance request to the Sentinel service.

        Args:
            payload: JSON‑serializable request body.

        Returns:
            Parsed JSON response.

        Raises:
            httpx.HTTPError: Network or protocol failure.
            ValueError: Invalid JSON response.
        """

        headers: Dict[str, str] = {
            "Content-Type": "application/json",
        }

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        url = f"{self.base_url}/compliance/check"

        logger.debug("Sending compliance request to %s", url)

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                url,
                json=payload,
                headers=headers,
            )
            response.raise_for_status()

            try:
                data: Dict[str, Any] = response.json()
            except ValueError as exc:
                logger.error("Invalid JSON response from Sentinel")
                raise ValueError(
                    "Invalid JSON response from Sentinel"
                ) from exc

        logger.debug("Compliance response received")
        return data
