#!/usr/bin/env python3

import sys
import password_database
import password_model

# load dataset, applicable for other honey word generation
passwords = password_database.load_rockyou_dataset()
print(passwords[password_model.PasswordModel.DIGITS_ONLY][:10])

# sample password to test with digit set dictionary
dictionary = passwords[password_model.PasswordModel.DIGITS_ONLY][:10]
actual_pass = '123456'

# actual function to generate the honeywords for digit only pass
def generateDigits(n, dict):
	passSize = len(actual_pass)
	honeyWordLst = []

	if len(actual_pass) == 0:
		actual_pass = "123456"

	i = 0
	while i < len(dictionary) and len(honeyWordLst) < n/2:
		word = dictionary[i]
		if word != actual_pass and (len(word) >= passSize - 3) and (len(word) <= passSize + 3):
			honeyWordLst.append(word)
		i += 1

	i = 0
	while len(honeyWordLst) <= n:
		honeyWordLst.append(actual_pass + str(i))
		i += 1

	return honeyWordLst

# test if the function returns correct list of honey words
honeyWordLst = generateDigits(10, dictionary)
print(honeyWordLst)