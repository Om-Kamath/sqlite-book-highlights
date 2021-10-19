import re


def validateFirstName(first_name):
    regex = re.compile(r'^[a-zA-Z]{2,}$')
    return bool(regex.match(first_name))


def validateAuthorName(author_name):
    regex = re.compile(r'^[a-zA-Z\s\.]{2,}$')
    return bool(regex.match(author_name))


def validateEmail(email):
    regex = re.compile(
        r'^[a-zA-Z_.0-9]+[@]\w+\.(com|edu|in|us|edu\.in|org)$')
    return bool(regex.match(email))


def validatePassword(password):
    # ?= makes sure that the code in front matches the previous characters
    # The conditions are:
    # Minimum 8 characters
    # At least one upperace and one lowercase character
    # At least one special character
    # At least one digit
    regex = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(regex.match(password))


def validateBookTitle(name):
    regex = re.compile(r'^[A-Za-z0-9\s\-_,\.;:()+*%$\'"]{2,}$')
    return bool(regex.match(name))
