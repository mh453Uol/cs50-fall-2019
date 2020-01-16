from nltk.tokenize import sent_tokenize

# * lines return lines (\n) which are in both strings a and b
# * lines assumes lines in a and b will be separated by \n
# * matched lines \n will be removed
# * list should not contain any duplicates
# * if both a and b contain one or more blank lines
#       (i.e., a \n immediately preceded by no other characters),
#       the returned list should include an empty string (i.e., "")
def lines(a, b):

    # 1. Split on lines i.e \n
    # 2. If fileALines contains any fileBLines[i] they match so append to matchedLines

    fileALines = { i:'' for i in a.splitlines() }
    fileBLines = { i:'' for i in b.splitlines() }

    matchedLines = {}

    for line in fileALines.keys():
        if line in fileBLines:
            if line not in matchedLines:
                matchedLines[line] = ''

    return list(matchedLines)


def sentences(a, b):
    # sentences are words which are ended with a . (dot)
    # 1. break file a & b into sentences
    # 2. check matching sentences in file a with file b

    fileASentences = sent_tokenize(a)
    fileBSentences = sent_tokenize(b)

    #print(fileASentences)
    #print(fileBSentences)

    fileASentencesSet = set(fileASentences)
    fileBSentencesSet = set(fileBSentences)

    #print(f"File A Set: {fileASentencesSet}")
    #print(f"File B Set: {fileBSentencesSet}")

    matches = fileASentencesSet.intersection(fileBSentencesSet)
    #print(matches)

    return matches

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    fileASubstrings = {}
    fileBSubstrings = {}

    substringOfN = ''

    for i in range(len(a)-n+1):
        substringOfN = a[i:i+n]
        if substringOfN not in fileASubstrings:
            fileASubstrings[substringOfN] = substringOfN

    for i in range(len(b)-n+1):
        substringOfN = b[i:i+n]
        if substringOfN not in fileBSubstrings:
            fileBSubstrings[substringOfN] = substringOfN

    intersection = []

    for substring in fileASubstrings:
        if substring in fileBSubstrings:
            intersection.append(substring)

    #print(fileASubstrings)
    #print(fileBSubstrings)
    #print(intersection)

    return intersection
