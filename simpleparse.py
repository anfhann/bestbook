import sys
import string

filename = sys.argv[1]

book = open(filename, 'r').read()
words = book.translate(string.maketrans("",""), string.punctuation).split()

for word in words:
	print word