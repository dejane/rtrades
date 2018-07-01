#required modules --> install from requirements.txt

from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy  import SQLAlchemy
import os
from flask_bootstrap import Bootstrap
from .config import *
from flask_cors import CORS, cross_origin



app = Flask(__name__)
Bootstrap(app)
CORS(app)
Scss(app)

if os.environ['WORKING_ENVIRONMENT'] == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

db = SQLAlchemy(app)

from .models import *

from .routes import *
from .api import *
