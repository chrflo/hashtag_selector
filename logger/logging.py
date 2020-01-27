import logging
import os

class Logger:
    def __init__(self, level='INFO', filename='hashtag_logs', path='logs'):
        self.logger = logging.getLogger('hashtag_application')
        self.logger.setLevel(self.getLvl(level))
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # check if logs folder exists and create it if not
        if not os.path.exists(path):
            os.mkdir(path)

        fh = logging.FileHandler(path + '/' + filename + '.txt')
        fh.setLevel(self.getLvl(level))
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def getLvl(self, level):
        if level.upper() == 'DEBUG':
            level = logging.DEBUG
        else:
            level = logging.INFO

        return level


# global log
# log = Logger().logger

