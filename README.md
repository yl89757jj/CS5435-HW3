# CS5435-HW3
HoneyWord Generator

password_database.py
input: rockyou-withcount.txt saved in local directory
output: map with dictionary word as key and count as value
purpose: generate a dictionary of words from the rockyou database (ignoring entries with only 1 entry)
v1 change: split only on the first white space, as rest are all passwords

password_model.py
input: password
output: password category as enum
purpose: filter passwords into categories so we can process logic based on type of password
v1 change: combined LETTERS_DIGITS_PATTERN, DIGITS_LETTERS_PATTERN, and LETTERS_DIGITS_LETTERS_PATTERN to MIXED_LETTERS_DIGITS;
		   combined SPECIAL_CHARS_END_PATTERN and SPECIAL_CHARS_START_PATTERN to WITH_SPECIAL_CHARS

program_1.py
input:
output:
purpose:
v1 change: 
