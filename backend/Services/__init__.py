# ==============================================================================

# PROPRIETARY AND CONFIDENTIAL

# OmniScan-XR System - Copyright (c) 2026 Serob Cholakyan

# This code is protected under the OmniScan-XR Proprietary License.

# Commercial use or unauthorized field mining operations are strictly prohibited.

# ==============================================================================

"""
Service layer package for OmniScan‑XR2.

This package contains reusable service classes responsible for
external communication, business logic, and integration with
third‑party systems such as Sentinel.
"""

from .Sentinel_Compliance_Handler import SentinelComplianceHandler

__all__ = [
    "SentinelComplianceHandler",
]
