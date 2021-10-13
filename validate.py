import re
def validatePassword(email):
    regex = re.compile('^[a-zA-Z_.0-9]+[@]\w+[.]{1,1}(com|edu|in|us|edu\.in|org)$')
    return bool(re.match(regex,email))


def validatePassword(password):
    # ?= makes sure that the code in front matches the previous characters
    #The conditions are: minimum 8 characters, atleast one upperace and one lowercase character, atleast one special character and atleast one digit
    regex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    return bool(re.match(regex,password))

