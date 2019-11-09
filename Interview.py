'''Implement an algorithm to determine if a string has all unique characters. '''
def isUnique(string):
    dict = {}
    repeats = True
    for char in string:
        if char in dict:
            repeats = False
        else:
            dict[char] = True
    return repeats

print(isUnique('helo'))
print(isUnique('hello'))

'''What if you cannot use additional data structures?'''
def isUniqueTwo(string):
    repeats = True
    i = 0
    j = 1
    while i < len(string):
        while j< len(string):
            if(string[i] == string[j]):
                repeats = False
            j+= 1
        i+= 1
        j = i + 1
        

    return repeats

print(isUniqueTwo('hello'))
print(isUniqueTwo('helo'))

''' Given two strings, write a method to decide if one is a permutation of the other '''

def permutation(first, second):
    if len(first) !== len(second):
        return False
    
    dict = {}
    palindrome = True
    for char in first:
        if dict.has_key(char):
            dict[char]+=1
        else:
            dict[char]= 1

    for char in second:
        if dict.has_key(char):
            dict[char] -= 1
            if dict[char] <= -1:
                palindrome = False
        else:
            palindrome = False
    return palindrome

print(permutation('hello', 'hello'))
print(permutation('oh', 'ho'))
print(permutation('hllo', 'hello'))


'''write a method to replace all the spaces in a string with %20 '''

def urlify(string):
  return string.replace(' ', '%20')

