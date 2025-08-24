# backend/app/api/endpoints/export.py
"""
API endpoints for code export functionality
"""

import logging
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
async def export_health_check():
    """Health check endpoint for export service"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }