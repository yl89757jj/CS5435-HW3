#!/usr/bin/env python3

def load_rockyou_dataset():
    passwords = {}
    with open('rockyou-withcount.txt', encoding='raw_unicode_escape') as passwords_file:
        for password_line in passwords_file:
            password_parts = password_line.lstrip().rstrip('\n').split(' ', 1)
            if (len(password_parts) == 2):
                if (password_parts[1] in passwords):
                    continue
                passwords[password_parts[1]] = int(password_parts[0])

        return passwords