import re
import time
import operator
import sys

words = {}

def run():
    start = time.clock()

    for file in sys.argv:
        count_words(file)

    end = time.clock()
    print_counts()
    total = end - start
    print 'counted all words in ' + unicode(total) + ' seconds'


def count_words(file_name):
    alpha_only = re.compile('[^a-zA-Z]')

    word_file = open(file_name)
    line_number = 1
    for line in word_file:
        for word in line.split():
            word = alpha_only.sub('', word)
            if word:
                words.setdefault(word, []).append(line_number)

        line_number += 1


def print_counts():
    for key in words.keys():
        line_to_num_occurrences = {}
        occurrences_of_word = words.get(key)
        for line in occurrences_of_word:
            if line_to_num_occurrences.get(line):
                line_to_num_occurrences[line] += 1
            else:
                line_to_num_occurrences[line] = 1

        output = key

        output += ' : ' + unicode(len(occurrences_of_word))
        for line in line_to_num_occurrences.keys():
            num_of_occurrences = line_to_num_occurrences.get(line)
            output += ' (' + unicode(line) + ', ' + unicode(num_of_occurrences) + '), '

        print output[:-2]

run()