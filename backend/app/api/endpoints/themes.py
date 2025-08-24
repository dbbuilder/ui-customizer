# backend/app/api/endpoints/themes.py
"""
API endpoints for theme generation and management
"""

import logging
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/health")
async def themes_health_check():
    """Health check endpoint for themes service"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }