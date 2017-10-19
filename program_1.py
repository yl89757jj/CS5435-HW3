#!/usr/bin/env python3

import sys
import password_database
import password_model

# TODO: Parse input parameters
print(sys.argv[1:])

# TODO: This is an example of loading the dataset and printing examples
passwords = password_database.load_rockyou_dataset()
print(passwords[password_model.PasswordModel.UNKNOWN][:10])
print(passwords[password_model.PasswordModel.DIGITS_ONLY][:10])
print(passwords[password_model.PasswordModel.LETTERS_ONLY][:10])
print(passwords[password_model.PasswordModel.MIXED_LETTERS_DIGITS][:10])
print(passwords[password_model.PasswordModel.WITH_SPECIAL_CHARS][:10])

# This is an example testing the password_model find method
# Outputs PasswordModel.DIGIT_ONLY
print(password_model.find('123456'))

# Outputs PasswordModel.LETTER_ONLY
print(password_model.find('helloworld'))

# Outputs PasswordModel.MIXED_LETTERS_DIGITS
print(password_model.find('123jennifer'))

# Outputs PasswordModel.MIXED_LETTERS_DIGITS
print(password_model.find('jennifer123'))

# Outputs PasswordModel.MIXED_LETTERS_DIGITS
print(password_model.find('cat5mouse'))

# Outputs PasswordModel.WITH_SPECIAL_CHARS
print(password_model.find('qwerty123!@#'))

# Outputs PasswordModel.WITH_SPECIAL_CHARS
print(password_model.find('!@#qwerty'))

# Outputs PasswordModel.WITH_SPECIAL_CHARS
print(password_model.find('    jhkjh     '))
