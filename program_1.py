#!/usr/bin/env python3

import utils

# TODO: this is an example of loading the dataset and printing the count of password '123456'
passwords = utils.load_rockyou_dataset()
print(passwords['123456'])