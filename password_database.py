#!/usr/bin/env python3

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