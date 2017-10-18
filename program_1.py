#!/usr/bin/env python3

import password_database
import password_model

# This is an example of loading the dataset and printing the count of password '123456'
#PASSWORDS = password_database.load_rockyou_dataset()
#print(PASSWORDS['123456'])

# This is an example testing the password_model find method
# Outputs PasswordModel.DIGIT_ONLY
print(password_model.find('123456'))

# Outputs PasswordModel.LETTER_ONLY
print(password_model.find('helloworld'))

# Outputs PasswordModel.DIGITS_LETTERS
print(password_model.find('123jennifer'))

# Outputs PasswordModel.LETTERS_DIGITS
print(password_model.find('jennifer123'))

# Outputs PasswordModel.LETTERS_DIGITS_LETTERS
print(password_model.find('cat5mouse'))

# Outputs PasswordModel.SPECIAL_CHARS_END
print(password_model.find('qwerty!@#'))

# Outputs PasswordModel.SPECIAL_CHARS_START
print(password_model.find('!@#qwerty'))

# Outputs PasswordModel.UNKNOWN
print(password_model.find('    jhkjh     '))
