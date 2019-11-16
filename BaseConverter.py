import math
import string

# TODO: Comment

def fromBaseToBase(originalBase, originalNumber, finalBase):
    numListS = [] # String number list
    numList = [] # Integer number list
    helpNum = 0 # Helper/auxiliary number in decimal (for logarithms and other operations)
    numIndex = 1 # Index for helping iterating over the number list
    oBase = originalBase # Original base number system
    oNum = string(originalNumber) # Original number
    fBase = finalBase # Final base number system
    fNum = "" # Final number

    ## Checks
    if oBase > 25: # Check if base < 26
        return "Sorry, this program doesn't support Base 26+; maybe in the future though!"
    if fBase > 25: # Check if base < 26
        return "Sorry, this program doesn't support Base 26+; maybe in the future though!"
    if oNum == 0: # If oNum == 0, then it equals zero in any base => return 0 everytime
        return "Your number {} in base {} is {} in base {}.".format(oNum, oBase, oNum, fBase)

    ## Logic
    if oBase != 10: # If the number is already in base10, skip this
        for x in oNum: # Iterating over the input number string and appending (to keep order) it to the string number list
            numListS.append(x)

        for x in numListS: # Convert numbers to base 10 numbers (and add them to numList)
            if x in string.ascii_uppercase:
                numList.append(int(string.ascii_uppercase.index(x)) + 10)
            elif x in string.ascii_lowercase:
                numList.append(int(string.ascii_lowercase.index(x)) + 10)
            else:
                numList.append(int(x))

        for x in numList: # Checking if the input number is valid in the selected number system
            if x >= oBase:
                return "Sorry, your number doesn't seem to be supported by the number system you selected."

        for x in numList: # Adding sequentially x*base^(index in original number from the left) -> converts the number to base 10
            helpNum += x*(oBase**(len(numList) - numIndex))
            numIndex += 1
    else: # Set in case of base 10
        helpNum = int(oNum)

    numListS = [] # Empty lists to reuse
    numList = []
    tLog = int(math.log(helpNum, fBase)) # First logarithm value

    while tLog >= 0:
        numList.append(int(helpNum/(fBase**tLog)))
        helpNum -= int(helpNum/(fBase**tLog))*(fBase**tLog)
        tLog -= 1

    for x in numList:
        if x > 9:
            numListS.append(string.ascii_uppercase[x - 10])
        else:
            numListS.append(str(x))

    fNum = fNum.join(numListS)

    return int(fNum)

originalBase = int(input("What base number system are you converting from (2 for binary, 3 for terniary, etc.)? "))
originalNumber = input("What is the number you want to convert? ")
finalBase = int(input("What base number system are you converting to (2 for binary, 3 for terniary, etc.)? "))
finalNumber = fromBaseToBase(originalBase, originalNumber, finalBase)

print("Your number {} (originally in base {}) is {} in base {}.".format(originalNumber, originalBase, finalNumber, finalBase))
