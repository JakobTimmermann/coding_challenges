################ Mein Ansatz ################
#'''
#Das müsste in O(N * n log(n)) Time laufen mit N len(bigString) und n len(smallString)
#'''
#
#bigString = "cbabcacabca"
#smallString = "abc"
#
#
#def find_occurences_of_string(bigString, smallStrings):
#    occurences = 0
#    lenSmallString = len(smallStrings[0])
#    for idx in range(0, len(bigString) - lenSmallString + 1): # O(N)
#        subString = bigString[idx:idx+lenSmallString]
#        subString = sorted(subString) # O(n log n) 
#        if "".join(subString) in smallStrings:
#            occurences += 1
#
#    return occurences
#
#
#number_of_occurences = find_occurences_of_string(bigString, [smallString])
#print(number_of_occurences)



##### ZWEITE LÖSUNG ###############
#'''
#Das müsste in O(N*n) Time laufen
#'''
#bigString = "cbabcacabca"
#smallString = "abc"
#
#def generate_mapping(string):
#    char_occurence = {}
#    for char in string:
#        char_occurence[char] = char_occurence.get(char, 0) + 1
#    return char_occurence
#
#def find_occurences_of_string(bigString, smallString):
#    occurences = 0
#    mappedSmallString = generate_mapping(smallString)
#    for idx in range(0, len(bigString) - len(smallString) + 1): # O(N)
#        subString = bigString[idx:idx+len(smallString)]
#        mappedSubString = generate_mapping(subString)
#        if mappedSmallString == mappedSubString:
#            occurences += 1
#
#    return occurences
#
#number_of_occurences = find_occurences_of_string(bigString, smallString)
#print(f"Number of occurences of '{smallString}' and its permutations in '{bigString}' is {number_of_occurences}")
#



bigString = "cbabcacabcaabcddddddabclllhllllbac"
smallString = "abc"

def generate_mapping(string):
    char_occurence = {}
    for char in string:
        char_occurence[char] = char_occurence.get(char, 0) + 1
    return char_occurence

def update_occurences(occurences, missingCharCounter, next_char, pop_char=None):
    if next_char in occurences.keys():
        occurences[next_char] -= 1
        if occurences[next_char] == 0:
            missingCharCounter += 1
        else:
            missingCharCounter -= 1
    if pop_char is not None and pop_char in occurences.keys():
        occurences[pop_char] += 1
        if occurences[pop_char] == 0:
            missingCharCounter += 1
        else:
            missingCharCounter -= 1
    return missingCharCounter

def find_occurences_of_string(bigString, smallString):
    occurences = 0
    currentOccurences = generate_mapping(smallString)
    missingCharCounter = 0
    for idx in range(0, len(bigString)):
        char = bigString[idx]
        if idx < len(smallString):
            missingCharCounter = update_occurences(currentOccurences, missingCharCounter, char)
        else:
            missingCharCounter = update_occurences(currentOccurences, missingCharCounter, char, bigString[idx-len(smallString)])
        if missingCharCounter == 3:
            occurences += 1
    return occurences

number_of_occurences = find_occurences_of_string(bigString, smallString)
print(f"Number of occurences of '{smallString}' and its permutations in '{bigString}' is {number_of_occurences}")





