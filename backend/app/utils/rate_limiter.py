# backend/app/utils/rate_limiter.py
"""
Rate limiting utility for API endpoints
"""

import asyncio
from typing import Dict
from datetime import datetime, timedelta

class RateLimiter:
    """Simple in-memory rate limiter"""
    
    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: Dict[str, list] = {}
    
    async def is_allowed(self, client_ip: str) -> bool:
        """Check if request is allowed for client IP"""
        now = datetime.now()
        
        # Clean old requests
        if client_ip in self.requests:
            self.requests[client_ip] = [
                req_time for req_time in self.requests[client_ip]
                if now - req_time < timedelta(seconds=self.window_seconds)
            ]
        else:
            self.requests[client_ip] = []
        
        # Check if under limit
        if len(self.requests[client_ip]) < self.max_requests:
            self.requests[client_ip].append(now)
            return True
        
        return False