testIDs = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

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

def runTestID(id):
	# converts the id to its dupes and displays the results
	print("ID:\t%s\ncounts:\t" %(id), idToDupesDict(id))

def main():
	for label in testIDs:
		runTestID(label)
	
main()