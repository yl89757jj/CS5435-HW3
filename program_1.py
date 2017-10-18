#!/usr/bin/env python3

import password_database
import password_model

# This is an example of loading the dataset and printing the count of password '123456'
PASSWORDS = password_database.load_rockyou_dataset()
print(PASSWORDS['123456'])

# This is an example testing the password_model find method
# Outputs PasswordModel.DIGIT_ONLY
print(password_model.find('123456'))

# Outputs PasswordModel.LETTER_ONLY
print(password_model.find('fjklrglidhgliA'))

# Outputs PasswordModel.DIGITS_LETTERS
print(password_model.find('435345sdjklsd'))

# Outputs PasswordModel.LETTERS_DIGITS
print(password_model.find('sdfshdfjk32423'))

# Outputs PasswordModel.LETTERS_DIGITS_LETTERS
print(password_model.find('cat5mouse'))

# Outputs PasswordModel.UNKNOWN
print(password_model.find('@#$*$*('))
