
from app.errors.conversion_errors import InvalidRangeError

# Wikipedia: https://en.wikipedia.org/wiki/Roman_numerals
# The roman symbols by place value
ROMAN_SYMBOLS = {0: ("I", "V", "X"), 1: ("X", "L", "C"), 2: ("C", "D", "M")}


def get_roman_numerals_place_val(digit: int, place_val: int) -> str:
	"""
	Get the roman numerals for a digit and place value
	:param digit: The digit
	:param place_val: Place value. Eg: 0 indicates 0th digit
	:return: Roman symbols
	"""
	if not 0 <= place_val <= 3:
		raise InvalidRangeError("0 <= place_val <=3", "Place value not within range")

	if not 0 <= digit <= 9:
		raise InvalidRangeError("0 <= digit <= 9", "Digit not within range")

	# Traverse digits
	if 0 <= place_val <= 2:
		roman_digits = ROMAN_SYMBOLS[place_val]
		if digit < 4:
			return digit * roman_digits[0]
		elif digit == 4:
			return roman_digits[0] + roman_digits[1]
		elif digit == 5:
			return roman_digits[1]
		elif digit < 9:
			return roman_digits[1] + (digit - 5) * roman_digits[0]
		else:
			return roman_digits[0] + roman_digits[2]
	else:
		return digit * ROMAN_SYMBOLS[2][2]


def get_roman_numerals(num_str: str) -> str:
	"""
	Get the roman numerals for a number
	:param num_str: The number to get roman numerals
	"""

	if not 1 <= int(num_str) <= 3999:
		raise InvalidRangeError("1 <= num <= 3999", "Input not within range")

	result = ""
	for place_val, digit_str in enumerate(reversed(num_str)):
		result = get_roman_numerals_place_val(int(digit_str),  place_val) + result
	return result


def get_output_json(num_str: str):
	"""
	Get the output in json for a number
	"""
	roman_num = get_roman_numerals(num_str)	
	output_json = {
		"input": num_str,
		"output": roman_num
	}
	return output_json
