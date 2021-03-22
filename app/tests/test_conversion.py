from app.conversion import get_roman_numerals_place_val, get_roman_numerals, get_output_json
from app.errors import InvalidRangeError

import unittest


def get_truth():
	# From https://en.wikipedia.org/wiki/Roman_numerals
	valid_val = "\
	Thousands	Hundreds	Tens	Units\n\
	1	M	C	X	I\n\
	2	MM	CC	XX	II\n\
	3	MMM	CCC	XXX	III\n\
	4	None	CD	XL	IV\n\
	5	None	D	L	V\n\
	6	None	DC	LX	VI\n\
	7	None	DCC	LXX	VII\n\
	8	None	DCCC	LXXX	VIII\n\
	9	None	CM	XC	IX \
	"

	rows = valid_val.split('\n')
	header = rows[0].split()
	truth = {name: {} for name in header}
	for row in rows[1:]:
		elements = row.split()
		for name, elem in zip(header, elements[1:]):
			truth[name][elements[0]] = elem
	return truth


class TestConversion(unittest.TestCase):

	TRUTH = get_truth()
	MAP = {'Units': 0, 'Tens': 1, 'Hundreds': 2, 'Thousands': 3}
	MAP_INV = ['Units', 'Tens', 'Hundreds', 'Thousands']

	def test_get_roman_numerals_place_val(self):
		"""
		
		"""
		for place, valid_conversions in self.TRUTH.items():
			for num_str, roman_numeral in valid_conversions.items():
				if roman_numeral != 'None':
					self.assertEqual(roman_numeral, get_roman_numerals_place_val(int(num_str), self.MAP[place]))

	def test_get_roman_numerals(self):

		for num in range(1, 4000):
			num_str = str(num)
			exp = ""
			for i, digit_str in enumerate(reversed(num_str)):
				if digit_str != '0':
					exp = self.TRUTH[self.MAP_INV[i]][digit_str] + exp
			self.assertEqual(exp, get_roman_numerals(num_str))

	def test_get_output_json(self):

		for num in range(1, 4000):
			num_str = str(num)
			self.assertEqual({"input": num_str, 'output': get_roman_numerals(num_str)}, get_output_json(num_str))

	def test_get_roman_numerals_place_val_exceptions(self):

		self.assertRaises(InvalidRangeError, get_roman_numerals_place_val, 1, -1)
		self.assertRaises(InvalidRangeError, get_roman_numerals_place_val, 2, 4)
		self.assertRaises(InvalidRangeError, get_roman_numerals_place_val, 30, 2)

	def test_get_roman_numerals_exceptions(self):

		self.assertRaises(InvalidRangeError, get_roman_numerals, '0')
		self.assertRaises(InvalidRangeError, get_roman_numerals, '4000')
		self.assertRaises(InvalidRangeError, get_roman_numerals, '20000')
		self.assertRaises(InvalidRangeError, get_roman_numerals, '-450')

	def test_get_output_json_exceptions(self):
		
		self.assertRaises(InvalidRangeError, get_output_json, '0')
		self.assertRaises(InvalidRangeError, get_output_json, '4000')
		self.assertRaises(InvalidRangeError, get_output_json, '20000')
		self.assertRaises(InvalidRangeError, get_output_json, '-450')
