from pymongo import MongoClient

def test_connection():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        print("Connection to MongoDB successful!")
        print("Collections:", db.list_collection_names())
    except Exception as e:
        print("Error connecting to MongoDB:", e)

if __name__ == "__main__":
    test_connection()
