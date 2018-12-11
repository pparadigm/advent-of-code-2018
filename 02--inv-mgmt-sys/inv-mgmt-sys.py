testIDs = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
realFile = "input.txt"

def idToDupesDict(id):
	# takes a string of characters
	# returns a dictionary with letters from the ID as the key, and the number
	#   of appearences as the value
	dupesDict = {}
	for letter in id:
		if letter in dupesDict:
			dupesDict[letter] += 1
		else:
			dupesDict[letter] = 1
	return dupesDict

def dictToDupesCount(dupeDict):
	# returns a tuple of doubleDupes, tripleDupes based on the dictionary counts
	doubleNotFound = True
	tripleNotFound = True
	doubleDupes = 0
	tripleDupes = 0
	for k, v in dupeDict.items():
		if v == 2 and doubleNotFound:
			doubleDupes += 1
			doubleNotFound = False
		elif v == 3 and tripleNotFound:
			tripleDupes += 1
			tripleNotFound = False
	return doubleDupes, tripleDupes

def genListFromFile(filename):
	# returns a list of the strings from the lines of the file
	results = []
	with open(filename) as inputFile:
		for line in inputFile:
			results.append(line.strip())
	return results
	
def main():
	doubleLetterIDsTot = 0
	tripleLetterIDsTot = 0
	
	listFromFile = genListFromFile(realFile)
	
	for label in listFromFile:
		# convert the id to its counts
		dupeLettersDict = idToDupesDict(label)
		# get the numbers of doubles and triples
		twos, threes = dictToDupesCount(dupeLettersDict)
		# add them to the total counts
		doubleLetterIDsTot += twos
		tripleLetterIDsTot += threes
	# calculate "checksum"
	checksum = doubleLetterIDsTot * tripleLetterIDsTot
	# display results
	print("# of double-letter IDs: %i\n"
		  "# of triple-letter IDs: %i\n"
		  "Checksum: %i" %(doubleLetterIDsTot, tripleLetterIDsTot, checksum))
	
	
main()