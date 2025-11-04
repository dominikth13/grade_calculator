#!/usr/bin/env python3
"""
Logging Configuration Module
Centralizes logging setup for the Student Grade Analyzer application.
"""

import logging
import warnings

def setup_logging():
    """
    Configure logging for the application.
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Capture warnings in the log
    logging.captureWarnings(True)
    
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    
    # Enable all warnings to be logged
    warnings.filterwarnings('default')
    
    return logging.getLogger(__name__)
