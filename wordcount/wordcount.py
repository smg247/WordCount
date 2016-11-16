import re
import time
import operator
import sys

counts = {}

def run():
    start = time.clock()

    for file in sys.argv:
        count_words(file)

    end = time.clock()
    print order_by_occurrences()
    total = end - start
    print 'counted all words in ' + unicode(total) + ' seconds'


def count_words(file_name):
    alpha_only = re.compile('[^a-zA-Z]')

    word_file = open(file_name)
    for line in word_file:
        for word in line.split():
            word = alpha_only.sub('', word)
            if word:
                if counts.get(word) is not None:
                    counts[word] += 1
                else:
                    counts[word] = 1


def order_by_occurrences():
    return sorted(counts.items(), key=operator.itemgetter(1), reverse=True)

run()