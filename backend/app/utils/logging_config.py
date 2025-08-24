# backend/app/utils/logging_config.py
"""
Logging configuration for the application
"""

import logging
import sys

def setup_logging():
    """Setup application logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )