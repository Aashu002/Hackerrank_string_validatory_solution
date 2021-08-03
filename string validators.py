if __name__ == '__main__':
    s = input() #input string from user 
    print(any(a.isalnum() for a in s) ) #to check is it alphanumeric
    print(any(a.isalpha() for a in s) ) # to check is alphabetic
    print(any(a.isdigit() for a in s) ) # to check is it digit 
    print(any(a.islower() for a in s) ) # to check the string is lower case
    print(any(a.isupper() for a in s) ) # to check the string is in upper case
