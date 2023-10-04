def multiply():
    result = 10*4
    return result
# Two blanks after close of functions


answer=multiply()
print(answer)


def is_palindrome(string_check):
    length=len(string_check)
    temp=True
    for index in range(length):
        if string_check[index] == string_check[length-1-index]:
        else:
            temp=False
            break
    return temp

def is_palindrome_class(string_check: str) -> bool:
    '''
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.
    :param string_check: string to check
    :return:True if `string` is a palindrome, False otherwise
    '''
    backwards=string_check[::-1]
    return backwards.casefold() ==string_check.casefold()


def is_palindrome_sentence(sentence):
    '''
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
    :param sentence:The sentence to check
    :return: True if `sentence` is a palindrome, False otherwise
    '''
    string=""
    #removing any spaces and retaining only alpha numerics
    for char in sentence:
        if char.isalnum():
            string+=char
    #return string.casefold()==string[::-1].casefold()
    return is_palindrome_class(string)



print('enter word to check palindrome')
word=input()
if is_palindrome_class(word):
    print("{} is palindrome".format(word))
else:
    print("{} is not palindrome".format(word))



