import logging
import sys


def setup_custom_logger(name):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(filename='%s.log'%name)
    stdout_handler = logging.StreamHandler(sys.stdout)
    handlers = [file_handler, stdout_handler]
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        handlers=handlers
    )
    file_handler.setFormatter(formatter)
    logger=logging.getLogger(name)
    logger.addHandler(file_handler)
    for handler in handlers:
        handler.close()
    return logger