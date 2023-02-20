
def check_pwd(password):
    if 7 < len(password) < 21:
        return contains_upper_case(password) and contains_lower_case(password) and contains_letter(password)
    else:
        return False

def contains_upper_case(text):
    return False if text.islower() else True

def contains_lower_case(text):
    return False if text.isupper() else True

def contains_letter(text):
    for char in text:
        if char.isalpha():
            return True
    return False
    