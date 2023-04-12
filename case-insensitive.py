import re

def word_to_regex(word):
    regex = ''
    for letter in word:
        regex += '[' + letter.upper() + letter.lower() + ']'
    return regex

def convert_to_regex(string):
    return re.sub(r'\b(?!S\b|W\b|Z\b|D\b|B\b|A\b|OR\b|AND\b|NOT\b)[a-zA-Z]+\b', lambda x: word_to_regex(x.group()), string)

def fix_regex(string):

    for each in re.findall('\\\\\\[\w{2}]', string):
        string = string.replace(each, '\\'+each[3])

    return string

# example usage
input_string = input("Enter Payload: ")
output_string = fix_regex(convert_to_regex(input_string))
print(output_string)
