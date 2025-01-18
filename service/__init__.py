# Perform initialization tasks
import logging

# Set up logging for the service package
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Service package initialized")
