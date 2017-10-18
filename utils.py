#!/usr/bin/env python3

import re
from enum import Enum

DIGIT_ONLY_PATTERN = re.compile('^\d+$')
LETTER_ONLY_PATTERN = re.compile('^[a-zA-Z]+$')

class PasswordModel(Enum):
    UNKNOWN = 0
    DIGIT_ONLY = 1
    LETTER_ONLY = 2

def find_password_model(password):
    match = DIGIT_ONLY_PATTERN.match(password)
    if (match):
        return PasswordModel.DIGIT_ONLY

    match = LETTER_ONLY_PATTERN.match(password)
    if (match):
        return PasswordModel.LETTER_ONLY

    return PasswordModel.UNKNOWN

# TODO: update this logic to handle passwords with spaces
def load_rockyou_dataset():
    passwords = {}
    with open('rockyou-withcount.txt', encoding='raw_unicode_escape') as passwords_file:
        for password_line in passwords_file:
            password_parts = password_line.strip().split(' ')
            if (len(password_parts) != 2):
                continue
            
            if (password_parts[1] in passwords):
                continue

            passwords[password_parts[1]] = int(password_parts[0])

        return passwords