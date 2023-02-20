
def check_pwd(password):
    if 7 < len(password) < 21:
        return contains_upper_case(password) and contains_lower_case(password) and contains_correct_chars(password)
    else:
        return False

def contains_upper_case(text):
    return False if text.islower() else True

def contains_lower_case(text):
    return False if text.isupper() else True

def contains_correct_chars(text):
    num = False
    letter = False
    for char in text:
        if char.isalpha():
            letter = True
        elif char.isdigit():
            num = True
    return num and letter
    