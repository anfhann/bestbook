import sys
import string
import operator

filename = sys.argv[1]

book = open(filename, 'r').read()
for c in string.punctuation:
	book = book.replace(c, " ")
words = book.split()

conc = {}

for raw in words:
	word = raw.lower()
	if len(word) > 3:  #Throw out the short words
		if conc.has_key(word):
			conc[word] = conc[word]+1
		else:
			conc[word] = 1

sorted_conc = sorted(conc.iteritems(), key=operator.itemgetter(1))

print "\n50 Most common words:\n"
for i in range(1, 50):
	print sorted_conc[len(sorted_conc) - i]
	
print "\nUnique words:\n"
count = 0
for key in conc.keys():
	if conc[key] == 1:
		count+=1
		print key

print "\n" + str(count) + " words used exactly once\n"