"""
Service layer package for OmniScan‑XR2.

Contains reusable service classes responsible for external communication
and business logic, including Sentinel compliance integration.
"""

from .Sentinel_Compliance_Handler import SentinelComplianceHandler

__all__ = [
    "SentinelComplianceHandler",
]
