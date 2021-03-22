from logging import getLogger

logger = getLogger()


class InvalidRangeError(Exception):
	def __init__(self, expression, message):
		"""
		Log custom app level error
		"""
		logger.error(message)
		self.expression = expression
		self.message = message
