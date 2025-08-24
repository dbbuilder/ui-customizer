# backend/app/services/generators/design_generator.py
"""
Advanced design generation service for creating unique, dynamic UI components
Uses algorithmic design principles to avoid cookie-cutter appearances
"""

import logging
import random
import colorsys
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass, asdict
from colour import Color
import json

logger = logging.getLogger(__name__)

@dataclass
class ColorPalette:
    """Represents a complete color palette for UI design"""
    primary: str
    secondary: str
    accent: str
    neutral: str
    background: str
    surface: str
    success: str
    warning: str
    error: str
    info: str
    text_primary: str
    text_secondary: str
    border: str
    shadow: str

@dataclass
class TypographyScale:
    """Typography system with font families and scale"""
    font_family_primary: str
    font_family_secondary: str
    font_family_mono: str
    scale_ratio: float
    base_size: str
    line_height_base: float
    line_height_heading: float
    letter_spacing_normal: str
    letter_spacing_wide: str
    
@dataclass
class SpacingSystem:
    """Consistent spacing system"""
    unit: int
    scale: List[int]
    container_padding: str
    section_padding: str
    component_padding: str
    
@dataclass
class BorderSystem:
    """Border radius and width system"""
    radius_xs: str
    radius_sm: str
    radius_md: str
    radius_lg: str
    radius_xl: str
    radius_full: str
    width_thin: str
    width_normal: str
    width_thick: str
    
@dataclass
class AnimationSystem:
    """Animation and transition system"""
    duration_fast: str
    duration_normal: str
    duration_slow: str
    easing_ease: str
    easing_ease_in: str
    easing_ease_out: str
    easing_ease_in_out: str
    easing_bounce: str
    
@dataclass
class DesignTokens:
    """Complete design token system"""
    colors: ColorPalette
    typography: TypographyScale
    spacing: SpacingSystem
    borders: BorderSystem
    animations: AnimationSystem
    shadows: Dict[str, str]
    breakpoints: Dict[str, str]

class DesignGeneratorService:
    """
    Advanced design generation service that creates unique, cohesive design systems
    """
    
    def __init__(self):
        """Initialize the design generator with base configurations"""
        self.design_styles = [
            'modern', 'minimalist', 'brutalist', 'glassmorphism', 
            'neumorphism', 'retro', 'organic', 'geometric'
        ]
        
        self.color_harmonies = [
            'monochromatic', 'analogous', 'complementary', 'triadic', 
            'split_complementary', 'tetradic', 'compound'
        ]
        
        self.typography_pairings = [
            ('Inter', 'Inter'), ('Poppins', 'Inter'), ('Roboto', 'Open Sans'),
            ('Montserrat', 'Source Sans Pro'), ('Nunito', 'Lato'),
            ('Work Sans', 'Merriweather'), ('Space Grotesk', 'Inter'),
            ('Plus Jakarta Sans', 'Inter'), ('Outfit', 'Inter')
        ]
        
        logger.info("Design generator service initialized")
    
    def generate_design_system(
        self, 
        base_config: Optional[Dict[str, Any]] = None,
        style_preference: Optional[str] = None,
        color_preference: Optional[str] = None
    ) -> DesignTokens:
        """
        Generate a complete, unique design system based on preferences
        
        Args:
            base_config: Optional base configuration to build upon
            style_preference: Preferred design style (modern, minimalist, etc.)
            color_preference: Base color for palette generation
            
        Returns:
            Complete design token system
        """
        try:
            logger.info(f"Generating design system with style: {style_preference}")
            
            # Determine design style
            style = style_preference or random.choice(self.design_styles)
            
            # Generate color palette
            colors = self._generate_color_palette(color_preference, style)
            
            # Generate typography system
            typography = self._generate_typography_system(style)
            
            # Generate spacing system
            spacing = self._generate_spacing_system(style)
            
            # Generate border system
            borders = self._generate_border_system(style)
            
            # Generate animation system
            animations = self._generate_animation_system(style)
            
            # Generate shadows
            shadows = self._generate_shadow_system(style, colors)
            
            # Generate breakpoints
            breakpoints = self._generate_breakpoint_system()
            
            design_tokens = DesignTokens(
                colors=colors,
                typography=typography,
                spacing=spacing,
                borders=borders,
                animations=animations,
                shadows=shadows,
                breakpoints=breakpoints
            )
            
            logger.info("Design system generated successfully")
            return design_tokens
            
        except Exception as e:
            logger.error(f"Error generating design system: {str(e)}")
            raise