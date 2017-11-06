import random
import string
import numpy as np
import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer

print('Secret Garden')
print('-------------')
print('              ')

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, "r")

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend([word] * freq)

    return random.choice(t)

def wordcount(filename):
    count = 0
    with open(filename, "r") as f:
        for char in f.read():
            count += 1
    return count

def sentiment(filename):
    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    score = SentimentIntensityAnalyzer().polarity_scores(data)
    print (score)

def main():
    hist = process_file('secretgarden.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    print(sentiment('secretgarden.txt'))    

    a = int(((wordcount('secretgarden.txt'))/total_words(hist)))
    print ('The average letters in a word is', a)

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    print('                    ')
    print('The length of the 20 most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', len(word))
    
    a = int(((wordcount('secretgarden.txt'))/total_words(hist)))
    print ('The average letters in a word is', a)
    print ("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')

if __name__ == '__main__':
    main()



print('              ')
print('              ')
print('              ')
print('              ')
print('Wikepeida Articles about the Secret Garden')
print('-------------')
print('              ')

def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, "r")

    for line in fp:
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist

def main():
    hist = process_file('secretgardenwiki.txt')
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    print(sentiment('secretgardenwiki.txt'))    

    a = int(((wordcount('secretgardenwiki.txt'))/total_words(hist)))
    print ('The average letters in a word is', a)

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    
    print('                    ')
    print('The length of the 20 most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', len(word))
    length = sum(len(word) for word in t[0:20])
    print ('The total amount of letters in the 20 most common words is', length)

    print("\n\nHere are some random words from the Wikipedia Page:")
    for i in range(100):
        print(random_word(hist), end=' ')

if __name__ == '__main__':
    main()

print('              ')
print('              ')
print('              ')
print('              ')
print('Ulysses')
print('-------------')
print('              ')

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, "r")

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist

def main():
    hist = process_file('ulysses.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    print(sentiment('ulysses.txt'))    

    a = int(((wordcount('ulysses.txt'))/total_words(hist)))
    print ('The average letters in a word is', a)

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    
    print('                    ')
    print('The length of the 20 most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', len(word))
    length = sum(len(word) for word in t[0:20])
    print ('The total amount of letters in the 20 most common words is', length)

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')

if __name__ == '__main__':
    main()

print('              ')
print('              ')
print('              ')
print('              ')
print('Wikepeida Articles about Ulysses')
print('-------------')
print('              ')

def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, "r")

    for line in fp:
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist

def main():
    hist = process_file('ulysses_wiki.txt')
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    print(sentiment('ulysses_wiki.txt'))     

    a = int(((wordcount('ulysses_wiki.txt'))/total_words(hist)))
    print ('The average letters in a word is', a)
    
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    print('                    ')
    print('The length of the 20 most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', len(word))
    length = sum(len(word) for word in t[0:20])
    print ('The total amount of letters in the 20 most common words is', length)

    print("\n\nHere are some random words from the Wikipedia Page:")
    for i in range(100):
        print(random_word(hist), end=' ')

if __name__ == '__main__':
    main()