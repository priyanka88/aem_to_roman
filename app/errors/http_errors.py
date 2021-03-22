from app import app
from app.errors.conversion_errors import InvalidRangeError
from flask import render_template
from logging import getLogger

logger = getLogger()


@app.errorhandler(TypeError)
def no_input_error(error):
	"""
	No input error handler
	"""
	print_error = "Missing parameter 'query'"
	logger.error(error)
	return render_template("error.html", error=print_error), 403


@app.errorhandler(ValueError)
def invalid_parameter(error):
	"""
	Invalid parameter error handler
	"""
	print_error = "Invalid parameter"
	logger.error(error)
	return render_template("error.html", error=print_error), 403


@app.errorhandler(InvalidRangeError)
def invalid_range_error(error):
	"""
	Invalid range error handler
	"""
	logger.error(error)
	return render_template("error.html", error=error), 403


@app.errorhandler(404)
def page_not_found(error):
	"""
	Page not found error handler
	"""
	print_error = "Page Not Found"
	logger.error(error)
	return render_template("error.html", error=print_error), 404


@app.errorhandler(500)
def internal_server_error(error):
	"""
	Internal server error handler
	"""
	print_error = "Internal Server Error"
	logger.error(error)
	return render_template("error.html", error=print_error), 500
