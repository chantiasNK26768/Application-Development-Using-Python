class Config:
    SECRET_KEY = 'dev_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234567890@localhost/student_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False