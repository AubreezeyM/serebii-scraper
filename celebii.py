import logging
import logging.config
logger = logging.getLogger(__name__)

from bs4 import BeautifulSoup

def get_page(url):
    logger.debug('reached get_page()')

if __name__ == '__main__':
    logging.basicConfig(format="%(name)s: %(levelname)s - %(message)s", level=logging.DEBUG)
    get_page('test')
    logger.debug('reached end of script')