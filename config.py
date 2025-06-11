import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '$7UNCB#yyJt9JFRrUUF6nURWmx1U9!8B&ddukQ&^nb8YCA*tf2kCT3uS*Xp114y%'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database/passwords.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False