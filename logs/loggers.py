import logging


def create_logger():
    basic_logger = logging.getLogger('basic')
    basic_logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('logs/api.log')
    formatter = logging.Formatter("%(asctime)s : %(message)s")
    file_handler.setFormatter(formatter)
    basic_logger.addHandler(file_handler)
