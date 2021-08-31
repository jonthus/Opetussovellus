from flask import Flask
from os import getenv
import re
import os

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

import routes
