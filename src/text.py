# function will convert string parameter to upper case
def to_upper(txt):
    if isinstance(txt, str):
        return txt.upper()
    raise TypeError('Hello, Error')

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    if not isinstance(str_list, list):
        raise TypeError('Hello, Error')
    
    for word in str_list:
        if word.islower():
            return False
    return True