import re 

string = "They give birth astride of a grave, the light gleams an instant, then it's night once more."
pattern = '\D'
result = re.match(pattern, string) #re.match search for the beginning of the string

if result: 
  print("Search successful")
else:
  print("Search unsuccessful")
  
# The best way to use RegEx is the following (using findall to return your results):
string = "Republicans Are Split On The Infrastructure Bill, But It's Mostly A Messaging Fight."
result = re.findall('\S', string)
print(result)

# if you need to use special characters as raw string, you should put an r before your RegEx.

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)

# list of patterns:
# [] set of characters, you can use - to set a range of characters
# . single character 
# ^x if a string starts with x character
# x$ if a string ends with x character
# * [SEARCH]
# + one or more occurrences of the pattern left to it 
# ? zero or one occurrence of the pattern left to it
# x{2,4} x at least 2 times and at most 4 times
# x|n x or n
# () group a pattern
# \ used to escape a metacharacter
# \A start of the string
# \b beginning or end (word/b) of a word
# \B NOT at the beginning or end (word/b) of a word
# \d decimal [0-9]
# \D non-decimal [^0-9]
# \s whitespace
# \S non-whitespace (a character)
# \w any alphanumeric character (digits, alphabets and _)
# \W non-alphanumeric character
# \Z end of a string. 
# before put it in your code, test using: https://regex101.com/

# list of methods 
# re.match(pattern, string) search for the beginning of the string
# re.findall() returns a list of strings containing all matches.
# re.split(pattern, string, maxnumberofsplits) splits the string where there is a match and returns a list of strings where the splits have occurred.
# re.sub(pattern, replace, string) returns a string where matched occurrences are replaced with the content of replace variable.
# re.sub(pattern, replace, string, 1)  You can pass count as a fourth parameter. If omited, it results to 0. This will replace all occurrences.
# re.subn(pattern, replace, string)  just like re.sub but returns a tuple with the new string and the old one
# re.search(pattern, string) the first location where the RegEx pattern produces a match with the string.
