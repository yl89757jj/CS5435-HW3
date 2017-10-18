#!/usr/bin/env python3

import re
from enum import Enum

DIGITS_ONLY_PATTERN = re.compile('^\d+$')
LETTERS_ONLY_PATTERN = re.compile('^[a-zA-Z]+$')
LETTERS_DIGITS_PATTERN = re.compile('^[a-zA-Z]+\d+$')
DIGITS_LETTERS_PATTERN = re.compile('^\d+[a-zA-Z]+$')
LETTERS_DIGITS_LETTERS_PATTERN = re.compile('^[a-zA-Z]+\d+[a-zA-Z]+$')

class PasswordModel(Enum):
    UNKNOWN = 0
    DIGITS_ONLY = 1
    LETTERS_ONLY = 2
    LETTERS_DIGITS = 3
    DIGITS_LETTERS = 4
    LETTERS_DIGITS_LETTERS = 5

def find(password):
    match = DIGITS_ONLY_PATTERN.match(password)
    if (match):
        return PasswordModel.DIGITS_ONLY

    match = LETTERS_ONLY_PATTERN.match(password)
    if (match):
        return PasswordModel.LETTERS_ONLY

    match = LETTERS_DIGITS_PATTERN.match(password)
    if (match):
        return PasswordModel.LETTERS_DIGITS

    match = DIGITS_LETTERS_PATTERN.match(password)
    if (match):
        return PasswordModel.DIGITS_LETTERS

    match = LETTERS_DIGITS_LETTERS_PATTERN.match(password)
    if (match):
        return PasswordModel.LETTERS_DIGITS_LETTERS

    return PasswordModel.UNKNOWN