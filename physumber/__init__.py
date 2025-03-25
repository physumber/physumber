"""
Physumber's entry point.
"""

import logging
import importlib

__version__ = "2025.0.0a1"
__all__ = ["sumbermath", "sumberphysics"]

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Initializing Physumber...")



def lazy_import(module_name):
    """
    Lazily imports a module.

    Args:
        module_name (str): The name of the module to import.

    Returns:
        module: The imported module.

    Raises:
        ImportError: If the module cannot be imported.
    """
    try:
        return importlib.import_module(module_name)
    except ImportError as err:
        LOGGER.error("Failed to import %s: %s", module_name, err)
        raise ImportError(f"Module {module_name} could not be loaded.") from err


# Placeholder for future configuration loading
CONFIG = None
