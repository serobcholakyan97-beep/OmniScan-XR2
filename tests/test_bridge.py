import pytest
from backend.Bridge.cloud_relay import get_bridge_status

def test_bridge_connection():
    """Verify the bridge status returns the expected dictionary."""
    status = get_bridge_status()
    assert status["bridge_active"] is True
    assert status["provider"] == "OmniScan-XR2-Internal"

def test_placeholder():
    """A simple truth test to ensure pytest is working."""
    assert 1 + 1 == 2
  
