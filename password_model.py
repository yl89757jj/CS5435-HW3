#!/usr/bin/env python3

import re
from enum import Enum

DIGITS_ONLY_PATTERN = re.compile('^\d+$')
LETTERS_ONLY_PATTERN = re.compile('^[a-zA-Z]+$')
LETTERS_DIGITS_PATTERN = re.compile('^[a-zA-Z]+\d+[a-zA-Z\d]*$')
DIGITS_LETTERS_PATTERN = re.compile('^\d+[a-zA-Z]+[a-zA-Z\d]*$')
SPECIAL_CHARS_PATTERN = re.compile('.*[^a-zA-Z\d]+.*')


class PasswordModel(Enum):
    UNKNOWN = 0
    DIGITS_ONLY = 1
    LETTERS_ONLY = 2
    MIXED_LETTERS_DIGITS = 3
    WITH_SPECIAL_CHARS = 4


def find(password):
    match = DIGITS_ONLY_PATTERN.match(password)
    if (match):
        return PasswordModel.DIGITS_ONLY

    match = LETTERS_ONLY_PATTERN.match(password)
    if (match):
        return PasswordModel.LETTERS_ONLY

    match = LETTERS_DIGITS_PATTERN.match(password)
    if (match):
        return PasswordModel.MIXED_LETTERS_DIGITS

    match = DIGITS_LETTERS_PATTERN.match(password)
    if (match):
        return PasswordModel.MIXED_LETTERS_DIGITS

    match = SPECIAL_CHARS_PATTERN.match(password)
    if (match):
        return PasswordModel.WITH_SPECIAL_CHARS

    return PasswordModel.UNKNOWN