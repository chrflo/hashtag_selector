from argparse import ArgumentParser


class ArgsParser:
    def __init__(self):
        parser = ArgumentParser()
        parser.add_argument("-f", "--file", dest="filename",
                            help="write report to FILE", metavar="FILE")
        parser.add_argument("-d", "--debug",
                            action="store_false", dest="verbose", default=True,
                            help="output debug information")

        self.args = parser.parse_args()