from openpyxl import load_workbook
import random
import datetime
import sys
from logger.logging import log
import arguments.argumentParser as parser

# Constants
HEADER_ROW = 1
HASHTAGS_IN_COL_ROW = 2
HASHTAGS_TO_USE_ROW = 3
START_ROW = 4
CATEGORY_NUM = 8
COL_NUM = CATEGORY_NUM * 2
END_COL = COL_NUM + 1
START_COL = 2
STEP = 2
SHEET_NAME = 'SheetWeighted'
SPACER = '•'
FILENAME = 'hashtags'
FILE_EXT = 'txt'


def normalize(weights):
    assert len(weights) > 0

    total = sum(weights)

    tempWeight = []
    for i in range(0, len(weights)):
        tempWeight.append(weights[i]/total)

    return tempWeight


def weighted_choice(seq, weights):
    log.debug('Seq Length: {1}, Weight Length: {0}, Probability Dist: {2}'.format(len(weights), len(seq), 1. - sum(weights)))
    assert len(weights) == len(seq)
    assert abs(1. - sum(weights)) < 1e-6

    x = random.random()
    for i, elmt in enumerate(seq):
        if x <= weights[i]:
            return elmt
        x -= weights[i]


def get_hashtags(count, weighted=False, filename=FILENAME):
    assert count != 0

    # open the file to write to and empty it's current contents
    file = open('{0}_{1}.{2}'.format(filename, datetime.date.today(), FILE_EXT), 'a')
    file.truncate(0)

    for m in range(0, count):
        hashtags = []
        for i in range(START_COL, END_COL, STEP):
            r = ws.cell(row=HASHTAGS_IN_COL_ROW, column=i).value
            num = ws.cell(row=HASHTAGS_TO_USE_ROW, column=i).value

            tempHashtags = []
            tempWeight = []
            log.debug('Number to pick: {0}, Rows: {1}'.format(num, r))
            for j in range(START_ROW, START_ROW+r):
                tempHashtags.append(ws.cell(row=j, column=i).value)
                tempWeight.append(ws.cell(row=j, column=i+1).value)

            #randomly select the hashtag
            for k in range(0, num):
                if not weighted:
                    index = random.randrange(len(tempHashtags))
                    hashtags.append('#' + tempHashtags.pop(index))
                else:
                    # normalize the weights
                    # this is placed here to ensure that the weights are normalized
                    # prior to entering the random weighted selection
                    tempWeight = normalize(tempWeight)

                    tag = weighted_choice(tempHashtags, tempWeight)
                    hashtags.append('#' + tag)

                    tagIndex = tempHashtags.index(tag)
                    tempHashtags.pop(tagIndex)
                    tempWeight.pop(tagIndex)

        hashtag = '\n{0}\n{0}\n{0}\n'.format(SPACER) + ' '.join(map(str, hashtags))
        file.write(hashtag)

    file.close()


appName = sys.argv[0]
args = parser.ArgsParser().parse(sys.argv[1:])
wb = load_workbook(args.workbook, data_only=True)
ws = wb[SHEET_NAME]
get_hashtags(args.iterations, args.weight, args.filename)

