import logging


def configure_logging():
    logger = logging.getLogger('main')
    logger.setLevel(logging.WARNING)
    logging.basicConfig(format='%(levelname)s:%(message)s')
