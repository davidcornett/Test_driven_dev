
def check_pwd(password):
    if 7 < len(password) < 21:
        return contains_upper_case(password) and contains_lower_case(password) and contains_correct_chars(password)
    else:
        return False

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
    