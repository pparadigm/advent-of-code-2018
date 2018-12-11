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

def findFraternalTwinIDs(idList):
	# returns the two IDs that are almost the same
	# we want to compare the first ID to every subsequent ID, and then compare
	#   the second ID to every subsequent ID, until we find a "match" that is
	#	off by only one character.
	listLen = len(idList)
	idLen = len(idList[0])
	firstIDMatch = ""
	secondIDMatch = ""
	matchesFound = False
	for firstID in range(listLen):
		if matchesFound: break
		comparer = idList[firstID]
		# I should be making sure we don't go past the end of the list but lazy
		for secondID in range(firstID + 1, listLen):
			if matchesFound: break
			comparee = idList[secondID]
			differenceFound = False
			for char in range(idLen):
				# if this is the first difference, note it and keep looking
				if ((comparer[char] != comparee[char]) and 
					(not differenceFound)):
					differenceFound = True
					# if this is the first difference, and we're at the end,
					#	return the IDs
					if char == idLen - 1: # freaking off-by-one error
						firstIDMatch = comparer
						secondIDMatch = comparee
						matchesFound = True
				# if this is the last character and only one difference has been
				#	found, return both IDs
				elif ((comparer[char] == comparee[char]) and 
					  (char == idLen - 1)):
					firstIDMatch = comparer
					secondIDMatch = comparee
					matchesFound = True
				# if this is the second difference, move onto the next ID to check
				elif ((comparer[char] != comparee[char]) and 
					  differenceFound):
					break
				# else if the characters are the same and not the last, go onto
				#	the next character
	return firstIDMatch, secondIDMatch

def getCommonSequence(a, b):
	# takes two strings of the same length that differ by a letter and 
	#	returns the letters in common
	common = ""
	lenA = len(a)
	for char in range(len(a)):
		# if two chars are same, add them to the common string
		if a[char] == b[char]:
			common += a[char]
		else:
			# if two chars are different and we're not at the last one, add all
			#	of the chars after this one to the common string and end the
			#	comparisons
			if not (char == (lenA-1)):
				common += a[char+1:lenA]
			break
	return common
	
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
	
	matchID1, matchID2 = findFraternalTwinIDs(listFromFile)
	print("\nMatch ID #1: %s\n"
		  "Match ID #2: %s" 
		  %(matchID1, matchID2))
	
	inCommon = getCommonSequence(matchID1, matchID2)
	print("Common ID sequence is: %s" %(inCommon))

	
main()