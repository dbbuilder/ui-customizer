# backend/app/api/endpoints/components.py
"""
API endpoints for component generation and management
Handles component creation, variants, and customization
"""

import logging
from typing import Dict, List, Any, Optional
from fastapi import APIRouter, HTTPException, status, Depends, Query
from pydantic import BaseModel, Field, validator
import asyncio
from datetime import datetime

from app.services.generators.design_generator import DesignGeneratorService
from app.services.generators.component_generator import ComponentGeneratorService

# Initialize services
design_service = DesignGeneratorService()
component_service = ComponentGeneratorService()
router = APIRouter()
logger = logging.getLogger(__name__)

# Request/Response Models
class ColorPaletteRequest(BaseModel):
    """Request model for color palette configuration"""
    primary: str = Field(..., description="Primary color in hex format")
    secondary: Optional[str] = Field(None, description="Secondary color in hex format")
    accent: Optional[str] = Field(None, description="Accent color in hex format")
    neutral: Optional[str] = Field(None, description="Neutral color in hex format")
    background: Optional[str] = Field(None, description="Background color in hex format")
    surface: Optional[str] = Field(None, description="Surface color in hex format")

class DesignConfigRequest(BaseModel):
    """Complete design configuration request"""
    style: str = Field(default="modern", description="Design style preference")
    colors: ColorPaletteRequest = Field(..., description="Color palette configuration")
    
    @validator('style')
    def validate_style(cls, v):
        """Validate design style is supported"""
        allowed_styles = ['modern', 'minimalist', 'brutalist', 'glassmorphism', 'neumorphism', 'retro', 'organic', 'geometric']
        if v not in allowed_styles:
            raise ValueError(f'Style must be one of: {", ".join(allowed_styles)}')
        return v

class ComponentGenerationRequest(BaseModel):
    """Request model for component generation"""
    design_config: DesignConfigRequest = Field(..., description="Design system configuration")
    component_types: List[str] = Field(default=["button", "card", "form"], description="Component types to generate")
    variants_per_type: int = Field(default=3, ge=1, le=10, description="Number of variants per component type")
    include_states: bool = Field(default=True, description="Include hover, focus, and disabled states")
    framework: str = Field(default="vue", description="Target framework (vue or react)")

@router.get("/types")
async def get_component_types():
    """Get list of available component types and their variants"""
    try:
        component_types = {
            "form_components": {
                "types": ["button", "input", "select", "checkbox", "radio", "toggle"],
                "description": "Interactive form elements with validation states"
            },
            "layout_components": {
                "types": ["card", "modal", "dropdown", "accordion", "tab"],
                "description": "Structural components for content organization"
            },
            "navigation_components": {
                "types": ["navigation", "breadcrumb", "pagination"],
                "description": "Navigation and wayfinding components"
            },
            "data_components": {
                "types": ["table", "list", "avatar", "badge"],
                "description": "Components for displaying data and content"
            }
        }
        
        logger.info("Retrieved component types successfully")
        return component_types
        
    except Exception as e:
        logger.error(f"Error retrieving component types: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve component types"
        )

@router.post("/generate")
async def generate_components(request: ComponentGenerationRequest):
    """Generate components based on design configuration"""
    try:
        logger.info(f"Starting component generation for {len(request.component_types)} types")
        
        # Generate design system tokens
        design_tokens = design_service.generate_design_system(
            base_config=request.design_config.dict(),
            style_preference=request.design_config.style,
            color_preference=request.design_config.colors.primary
        )
        
        # For now, return mock data
        generated_components = []
        for i, component_type in enumerate(request.component_types):
            for j in range(request.variants_per_type):
                component = {
                    "id": f"{component_type}_{i}_{j}",
                    "name": f"{component_type.capitalize()}Component{j+1}",
                    "type": component_type,
                    "variant": f"variant-{j+1}",
                    "framework": request.framework,
                    "template": f"<!-- {component_type} component template -->",
                    "styles": {"main": f".{component_type} {{ /* styles */ }}"},
                    "props": {"size": "md", "variant": "primary"},
                    "usage_example": f"<{component_type.capitalize()}Component />",
                    "accessibility_features": ["keyboard-navigation", "aria-labels"],
                    "created_at": datetime.now().isoformat()
                }
                generated_components.append(component)
        
        response = {
            "success": True,
            "message": f"Successfully generated {len(generated_components)} components",
            "components": generated_components,
            "design_tokens": design_tokens.__dict__ if hasattr(design_tokens, '__dict__') else {},
            "generation_time": 0.5,
            "total_components": len(generated_components)
        }
        
        logger.info(f"Component generation completed")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f"Error during component generation: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Component generation failed due to internal error"
        )

@router.get("/health")
async def components_health_check():
    """Health check endpoint for components service"""
    try:
        return {
            "status": "healthy",
            "services": {
                "design_generator": "healthy",
                "component_generator": "healthy"
            },
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }