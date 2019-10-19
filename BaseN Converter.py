import math
import string

def convertNumbers():
    nListS = [] # String number list (reused)
    nList = [] # Number list in integers (reused)
    hNum = 0 # Helper/auxiliary number in decimal (for logarithms and other functions)
    nInd = 1 # Index for helping iterating over the number list
    oSys = int(input("What base number system are you converting from (2 for binary, 3 for terniary, etc.)? ")) # Orignal base number system
    if oSys > 25: # Check if base < 26
        return "Sorry, this program doesn't support Base 26+; maybe in the future though!"
    fSys = int(input("What base number system are you converting to (2 for binary, 3 for terniary, etc.)? ")) # Final base number system
    if fSys > 25: # Check if base < 26
        return "Sorry, this program doesn't support Base 26+; maybe in the future though!"
    oNum = input("What is the number you want to convert? ") # Original number
    fNum = ""


    if oNum == 0: # If oNum == 0, then it equals zero in any base => return 0 everytime
        return "Your number {} in base {} is {} in base {}.".format(oNum, oSys, oNum, fSys)

    if oSys != 10: # If the number is already in base10, skip this
        for x in oNum: # Iterating over the input number string and appending (to keep order) it to the string number list
            nListS.append(x)

        for x in nListS: # Convert numbers to base 10 numbers (and add them to nList)
            if x in string.ascii_uppercase:
                nList.append(int(string.ascii_uppercase.index(x)) + 10)
            elif x in string.ascii_lowercase:
                nList.append(int(string.ascii_lowercase.index(x)) + 10)
            else:
                nList.append(int(x))

        for x in nList: # Checking if the input number is valid in the selected number system
            if x >= oSys:
                return "Sorry, your number doesn't seem to be supported by the number system you selected."

        for x in nList: # Adding sequentially x*base^(index in original number from the left) -> converts the number to base 10
            hNum += x*(oSys**(len(nList) - nInd))
            nInd += 1 # Basically nInd++
    else: # Set in case of base 10
        hNum = int(oNum)

    nListS = [] # Empty lists to reuse
    nList = []
    tLog = int(math.log(hNum, fSys)) # First logarithm value

    while tLog >= 0:
        nList.append(int(hNum/(fSys**tLog)))
        hNum -= int(hNum/(fSys**tLog))*(fSys**tLog)
        tLog -= 1

    for x in nList:
        if x > 9:
            nListS.append(string.ascii_uppercase[x - 8])
        else:
            nListS.append(str(x))

    fNum = fNum.join(nListS)

    return "Your number {} in base {} is {} in base {}.".format(oNum, oSys, fNum, fSys)

print(convertNumbers()) # All in all 51 lines of code
