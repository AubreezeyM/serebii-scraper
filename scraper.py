import logging
import logging.config
import os

from bs4 import BeautifulSoup

logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.debug("logger created!")
    print("End of script")