
from flask import Flask

app = Flask(__name__)

from app import routes
from app.errors import http_errors
