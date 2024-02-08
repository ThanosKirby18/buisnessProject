def verifyNumber(num): #checks to see if an import is a number raises an erro if not
    try:
        newNum = int(num)
    except ValueError:
        raise RuntimeError("Incompatible Data Type was entered")
def verifyText(text): #raises an error if there is a digit is in the string
    if any(char.isdigit() for char in text):
        raise RuntimeError("Incompatible Data Type Digit was entered")
    return True