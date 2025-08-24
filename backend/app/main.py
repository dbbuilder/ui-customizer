# backend/app/main.py
"""
Main FastAPI application for UI Customizer Tool
Provides API endpoints for generating dynamic UI components and themes
"""

import logging
import os
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError

from app.api.endpoints import components, themes, export
from app.utils.logging_config import setup_logging
from app.utils.rate_limiter import RateLimiter

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)

# Rate limiter instance
rate_limiter = RateLimiter(max_requests=100, window_seconds=60)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager
    Handles startup and shutdown events
    """
    # Startup
    logger.info("Starting UI Customizer Tool API")
    
    # Initialize any startup processes here
    # - Database connections
    # - Cache warming
    # - Template loading
    
    yield
    
    # Shutdown  
    logger.info("Shutting down UI Customizer Tool API")
    # Clean up resources here

# Create FastAPI application instance
app = FastAPI(
    title="UI Customizer Tool API",
    description="API for generating dynamic, customizable UI components for Vue.js and React",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Security middleware
app.add_middleware(
    TrustedHostMiddleware, 
    allowed_hosts=["localhost", "127.0.0.1", "*.vercel.app", "*.netlify.app"]
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Mount static files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Global exception handler
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError) -> JSONResponse:
    """
    Handle Pydantic validation errors
    Returns structured error response with validation details
    """
    logger.error(f"Validation error on {request.url}: {exc}")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation Error",
            "message": "Invalid input parameters",
            "details": exc.errors(),
            "request_id": getattr(request.state, 'request_id', None)
        }
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Handle HTTP exceptions with structured error response
    """
    logger.error(f"HTTP error {exc.status_code} on {request.url}: {exc.detail}")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTP Error",
            "message": exc.detail,
            "status_code": exc.status_code,
            "request_id": getattr(request.state, 'request_id', None)
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Handle unexpected exceptions
    Returns generic error response while logging full details
    """
    logger.exception(f"Unexpected error on {request.url}: {str(exc)}")
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred",
            "request_id": getattr(request.state, 'request_id', None)
        }
    )

# Middleware for request logging and rate limiting
@app.middleware("http")
async def request_middleware(request: Request, call_next):
    """
    Middleware for request processing
    Handles rate limiting, request logging, and adds request ID
    """
    # Generate unique request ID
    import uuid
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    
    # Get client IP address
    client_ip = request.client.host if request.client else "unknown"
    
    # Apply rate limiting
    if not await rate_limiter.is_allowed(client_ip):
        logger.warning(f"Rate limit exceeded for IP: {client_ip}")
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={
                "error": "Rate Limit Exceeded",
                "message": "Too many requests. Please try again later.",
                "request_id": request_id
            }
        )
    
    # Log request
    logger.info(f"Request {request_id}: {request.method} {request.url} from {client_ip}")
    
    # Process request
    try:
        response = await call_next(request)
        logger.info(f"Response {request_id}: {response.status_code}")
        
        # Add request ID to response headers
        response.headers["X-Request-ID"] = request_id
        
        return response
    except Exception as e:
        logger.exception(f"Error processing request {request_id}: {str(e)}")
        raise

# Include API routers
app.include_router(
    components.router, 
    prefix="/api/v1/components", 
    tags=["components"]
)

app.include_router(
    themes.router, 
    prefix="/api/v1/themes", 
    tags=["themes"]
)

app.include_router(
    export.router, 
    prefix="/api/v1/export", 
    tags=["export"]
)

# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint for monitoring
    Returns application status and basic system information
    """
    try:
        # Add any health checks here (database, external services, etc.)
        return {
            "status": "healthy",
            "version": "1.0.0",
            "timestamp": "2024-12-23T10:00:00Z",
            "environment": os.getenv("ENVIRONMENT", "development")
        }
    except Exception as e:
        logger.exception(f"Health check failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service temporarily unavailable"
        )

# Root endpoint
@app.get("/", tags=["root"])
async def root() -> Dict[str, str]:
    """
    Root endpoint with API information
    """
    return {
        "message": "UI Customizer Tool API",
        "version": "1.0.0",
        "docs": "/api/docs",
        "redoc": "/api/redoc",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    
    # Development server configuration
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info",
        access_log=True
    )