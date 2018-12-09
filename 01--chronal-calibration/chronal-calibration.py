#!usr/bin/python3

# imports


# initialize variables
testFile1 = "test1.txt"
testFile2 = "test2.txt"
testFile3 = "test3.txt"
realFile = "input.txt"

# get data


# calculate


# display results


def totalFile(filename):
    try:
        with open(filename) as currentFile:
            total = 0
            for line in currentFile:
                if line != "\n":
                    num = int(line[:-1])
                    total += num
            return total

    except FileNotFoundError:
        print("\nError: File not found: ", filename)
        return None


def main():
    t1Answer = totalFile(testFile1)
    if t1Answer != None:
        print("The total for test1 is %i." %(t1Answer))
    t2Answer = totalFile(testFile2)
    if t2Answer != None:
        print("The total for test2 is %i." %(t2Answer))
    t3Answer = totalFile(testFile3)
    if t3Answer != None:
        print("The total for test3 is %i." %(t3Answer))
    realAnswer = totalFile(realFile)
    if realAnswer != None:
        print("The final total is %i." %(realAnswer))


main()
