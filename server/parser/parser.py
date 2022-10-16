
# resource(s):
# use of regex with explanation:
# https://stackoverflow.com/questions/53711841/how-to-find-price-tag-with-dollar-sign-thousand-delimiter-and-decimal-point-by
#

import re

with open('test_parse.txt', 'r') as file:
    text_str = file.read()

    prices = re.findall(r"\b\$?[\d,.]+\b", text_str)

    print(prices)
