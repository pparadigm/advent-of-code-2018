#!usr/bin/python3

# imports


# initialize variables
total = 0
testFile1 = "test1.txt"
testFile2 = "test2.txt"
testFile3 = "test3.txt"
realFile = "input.txt"

# get data


# calculate


# display results


def totalFile(filename):
    try:
        currentFile = open(filename, 'r')
        return 1
    except FileNotFoundError:
        print("\nError: File not found: ", filename)
        return None


    currentFile.close()


def main():
    answer = totalFile(realFile)
    if answer:
        print("The total is %i." %(answer))


main()
