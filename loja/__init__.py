from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
app.config['SECRET_KEY'] = 'oidfjddifj123'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(BASE_DIR, 'static/media')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


from loja.admin import route
from loja.produtos import route
