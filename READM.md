# Authors we colaborated (its a coloboration project)


# all installed Depandancies

command to initializa db -- `flask db init`
run migration -- `flask db revision --autogenerate -m "message"`
` 
flask = `pip install flask`
sqlalchemy = `pip install flask-sqlalchemy`
flask-migrate = `pip install flask-migrate`
flask restful = `pip install flask-restful`
flask-Bycrpt = `pip install Flask-bcrypt`
flask cors = `pip install flask-cors`
flask jwt manager = `pip install flask-jwt-extended`  ...  `Dont forget to configure it

JWT CONFIGURATION
from datetime import timedelta
from flask_jwt_extended import JWTManager
app.config["JWT_SECRET_KEY"] = "super-secret"  # we should remember to change this
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30) ...should have  the least time eg minutes = 1

jwt = JWTManager(app)

`   @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserModel.query.filter_by(id=identity).one_or_none().to_json()
`

