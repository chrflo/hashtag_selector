import logging


class Logger:
    def __init__(self, level=logging.DEBUG, filename='hashtag_logs'):
        self.logger = logging.getLogger('hashtag_application')
        self.logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        fh = logging.FileHandler(filename + '.txt')
        fh.setLevel(level)
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)


global log
log = Logger().logger

