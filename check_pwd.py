
def check_pwd(pwd):
    return check_length(pwd) and contains_upper_case(pwd) and contains_lower_case(pwd) and contains_correct_chars(pwd)


def check_length(text):
    min = 8
    max = 20
    return True if len(text) >= min and len(text) <= max else False

def contains_upper_case(text):
    return False if text.islower() else True

def contains_lower_case(text):
    return False if text.isupper() else True

# returns true only if string contains at least one num, letter, and special char
def contains_correct_chars(text):
    special_list = "~`!@#$%^&*()_+-="
    num = False
    letter = False
    special = False
    for char in text:
        if char.isalpha():
            letter = True
        elif char.isdigit():
            num = True
        elif char in special_list:
            special = True
    return num and letter and special
    