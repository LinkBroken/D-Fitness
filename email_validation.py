import re
# Validating the emails using Regular Expressions
def validate(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') 
    if re.fullmatch(regex, email): # the fullmatch function checks if the email given matches the criteria for a valid email
        return True
    return False

