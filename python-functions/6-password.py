def validate_password(password):
    validate = True
    if len(password) > 8:
        return validate
    if not any(char.isupper()for char in password):
        return not validate
    if not any(char.islower()for char in password):
        return not validate
    if not any(char.isdigit()for char in password):
        return not validate
    if not any(char.isspace()for char in password):
        return not validate
    if validate:
        return True
    else: 
        return False
