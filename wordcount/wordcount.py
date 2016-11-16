import re
def run():
    count_words('../words.txt')


def count_words(file_name):
    alpha_only = re.compile('[^a-zA-Z]')
    counts = {}
    word_file = open(file_name)
    for line in word_file:
        for word in line.split():
            word = alpha_only.sub('', word)
            if word:
                if counts.get(word) is not None:
                    counts[word] += 1
                else:
                    counts[word] = 1

    print counts

run()