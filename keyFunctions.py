from hmac import digest
from unicodedata import digit


class keyFunctions:


    def countChars(self,str):
        """ Takes a given string and returns the count of special symbols, digits, and chars in a dictionary """
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        charsAndCountDict = {}
        for i in str:
          if i in symbols:
            if 'symbols' not in charsAndCountDict:
              charsAndCountDict['symbols'] = 1
            else:
              charsAndCountDict['symbols'] += 1
          elif i in digits:
            if 'digits' not in charsAndCountDict:
              charsAndCountDict['digits'] = 1
            else:
              charsAndCountDict['digits'] += 1
          else:
            if 'chars' not in charsAndCountDict:
              charsAndCountDict['chars'] = 1
            else:
              charsAndCountDict['chars'] += 1
        return charsAndCountDict

str1 = "P@#yn26at^&i5ve"
if __name__ == '__main__':
  func1 = keyFunctions()
  print(func1.countChars(str1))