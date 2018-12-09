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
            for line in currentFile:
                if line != "\n":
                    num = int(line[:-1])
                    print(num)

    except FileNotFoundError:
        print("\nError: File not found: ", filename)
        return None


def main():
    answer = totalFile(testFile1)
    if answer:
        print("The total is %i." %(answer))


main()
