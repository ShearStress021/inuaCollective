from flask_bcrypt import Bcrypt
from flask_migrate import Migrate 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()
migrate = Migrate(render_as_batch=True)
login_manager = LoginManager()
bcrypt = Bcrypt()
