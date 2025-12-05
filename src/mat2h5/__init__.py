"""
mat2h5 - MATLAB to H5 Conversion Tool

A standalone tool for converting MAGAT (MATLAB Track Analysis) experiment data
to H5 format for use in Python analysis pipelines.
"""

__version__ = "1.0.0"
__author__ = "Gil Raitses"

# Lazy imports to avoid requiring MATLAB Engine at import time
def __getattr__(name):
    if name == 'MAGATBridge':
        from .bridge import MAGATBridge
        return MAGATBridge
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

__all__ = ['MAGATBridge']

