#!/usr/bin/env python3

import password_model as pm

def load_rockyou_dataset():
    passwords = {
        pm.PasswordModel.UNKNOWN : [],
        pm.PasswordModel.DIGITS_ONLY : [],
        pm.PasswordModel.LETTERS_ONLY : [],
        pm.PasswordModel.MIXED_LETTERS_DIGITS : [],
        pm.PasswordModel.WITH_SPECIAL_CHARS : []
    }
    
    with open('rockyou-withcount.txt', encoding='raw_unicode_escape') as passwords_file:
        for password_line in passwords_file:
            password_parts = password_line.lstrip().rstrip('\n').split(' ', 1)
            if (len(password_parts) != 2):
                continue

            password = password_parts[1]
            password_model = pm.find(password)
            passwords[password_model].append(password)

        return passwords
