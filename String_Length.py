class StringClass:
    def __init__(self, input):        self.input = input

    def lengthOfString(self):
        return len(self.input)

    def convertStringToListOfChars(self):
        list1 = []
        list1[:0] = self.input
        return list1
str1 = StringClass("12345")
print("Length of string is: ", str1.lengthOfString())
listOfChar = str1.convertStringToListOfChars()
print("List of characters: ", listOfChar)
