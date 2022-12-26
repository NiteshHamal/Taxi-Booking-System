import re


def namevalidation(name):
    regex = re.compile(
        "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)")
    if re.fullmatch(regex, name):
        nameResult = True
    else:
        nameResult = False
    return nameResult


def emailvalidation(email):
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        emailResult = True
    else:
        emailResult = False
    return emailResult


def numbervalidation(number):
    regex = re.compile('^(?:0|\+?977)\s?(?:\d\s?){9,11}$')
    if re.fullmatch(regex, number):
        numberResult = True
    else:
        numberResult = False
    return numberResult


def passwordvalidation(password):
    regex = re.compile(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    if re.fullmatch(regex, password):
        passwordResult = True
    else:
        passwordResult = False
    return passwordResult


def timevalidation(time):
    regex = re.compile("(0[1-9]|1[0-2]):([0-5][0-9]) ((a|p)m|(A|P)M)")
    if re.fullmatch(regex, time):
        timeResult = True
    else:
        timeResult = False
    return timeResult
