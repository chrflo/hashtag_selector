from argparse import ArgumentParser


class ArgsParser:
    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument("-f", "--file", dest="filename",
                            help="write hashtags to FILE", metavar="FILE", type=str, required=True)
        self.parser.add_argument("-wb", "--workbook", dest="workbook",
                            help="hashtag workbook", metavar="FILE", type=str, required=True)
        self.parser.add_argument("-d", "--debug", dest="logLvl", default='INFO',
                            help="output debug information", type=str, required=False)
        self.parser.add_argument("-w", "--weighted", dest="weight", default=True,
                            help="should this be a weighted selection", type=bool, required=True)
        self.parser.add_argument("-i", "--iterations", dest="iterations", default=1,
                            help="number of times to generate a hashtag set", type=int, required=False)
        self.parser.add_argument("-lp", "--logPath", dest="logPath", default='logs',
                            help="the path of the log files", type=str, required=False)

    def parse(self, args):
        return self.parser.parse_args(args)


