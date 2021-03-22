from app import app
from app.conversion import get_output_json
from flask import request


@app.route('/romannumeral')
def get():
	"""
	Route to get input from user
	"""
	integer = request.args.get('query')
	return get_output_json(integer)
