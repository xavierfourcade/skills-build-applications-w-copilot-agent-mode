from pymongo import MongoClient

# Establish MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

# Example collections
users_collection = db['users']
teams_collection = db['teams']
activity_collection = db['activity']
leaderboard_collection = db['leaderboard']
workouts_collection = db['workouts']

# Example function to insert a user
def insert_user(email, name, age):
    user = {"email": email, "name": name, "age": age}
    users_collection.insert_one(user)
