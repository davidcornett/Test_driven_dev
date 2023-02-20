
def check_pwd(password):
    if 7 > len(password) < 21:
        return True
    else:
        return False