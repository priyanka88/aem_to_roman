from app import routes

import unittest


class TestRoutes(unittest.TestCase):

	def test_get_valid_and_errors(self):
		with routes.app.test_client() as c:
			for integer in range(1, 4000):
				response = c.get('/romannumeral?query={}'.format(integer))
				self.assertEqual(response.status_code, 200)

			# No input error
			response = c.get('/romannumeral?blah=100')
			self.assertEqual(response.status_code, 403)

			# Invalid parameter
			response = c.get('/romannumeral?query=abc')
			self.assertEqual(response.status_code, 403)

			# Invalid range error
			response = c.get('/romannumeral?query=5000')
			self.assertEqual(response.status_code, 403)

			# Page not found error
			response = c.get('/roman')
			self.assertEqual(response.status_code, 404)
