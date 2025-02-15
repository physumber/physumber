"""
Physumber's entry point
"""

import logging
import importlib

__version__ = "0.1.0"

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("pyPhysumber")
logger.info("Initializing Physumber...")

# Lazy Import Function
def lazy_import(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        logger.error(f"Failed to import {module_name}: {e}")
        raise ImportError(f"Module {module_name} could not be loaded.")

# Placeholder for configuration (until load_config is implemented)
config = None
