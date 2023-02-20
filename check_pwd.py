
def check_pwd(password):
    if 7 < len(password) < 21:
        return check_lowercase(password)
    else:
        return False

def check_lowercase(text):
    return False if text.islower() else True
