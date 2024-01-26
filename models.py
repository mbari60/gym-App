from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String , nullable = False)

    #the workouts a user has selected
    user_workouts = db.relationship('UserWorkout', back_populates='user')

    workouts = db.relationship('WorkoutModel', secondary='user_workout', back_populates='users')
    #uselist one to one -- one user can have only one profile
    profile = db.relationship('ProfileModel', backref='user', uselist=False)

class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String , nullable=False)
    image = db.Column(db.String , nullable=False)
    trainer = db.Column(db.String, nullable = False)
    Price = db.Column(db.Integer, nullable=False)
    time= db.Column(db.String, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default= db.func.now())

    #workouts the user have selected 
    workout_users = db.relationship('UserWorkout', back_populates='workout')
    #relationship between the currentmodel and UserModel
    users = db.relationship('UserModel', secondary='user_workout', back_populates='workouts')

class UserWorkout(db.Model):
    __tablename__ = 'user_workout'
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), primary_key=True)

    user = db.relationship('UserModel', back_populates='user_workouts')
    workout = db.relationship('WorkoutModel', back_populates='workout_users')

class ProfileModel(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    phone = db.Column(db.String ,unique = True)
    dob = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    #user has only one profile
    user = db.relationship('UserModel', backref='profile', uselist=False)
