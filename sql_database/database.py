# TODO talk to SQLite db
# doesn't want to think about how data is presented nor how to talk to UI 
# sends info back to view_model

# abc database would be a model of what any database should have in terms of methods - may leave this for last
# this would allow another type of db to be put in place of the sqlite db (this file)

import sqlite3 
# from .config import db  # .config means import from this directory 
from .config import db_path
from exceptions.quiz_error import QuizError

# from database import VehicleDB TODO rewatch videos on abstract methods
from model.quiz_model import Quizquestion

# from utils.validation import TODO write validation for ints and more specifically for ints within a certain range

