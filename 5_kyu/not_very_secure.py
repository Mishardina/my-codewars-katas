def alphanumeric(password):
    if not password:
        return False
    
    for i in range(len(password)):
        if (password[i] < 'a' or password[i] > 'z') and (password[i] < '0' or password[i] > '9') and (password[i] < 'A' or password[i] > 'Z'):
            return False
    
    return True