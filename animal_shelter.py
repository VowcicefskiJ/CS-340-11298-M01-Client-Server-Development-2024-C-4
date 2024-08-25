from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, db_name, collection_name):
        # Initialize the MongoClient and connect to the database and collection
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]

    def create(self, data):
        """ Insert a document into the collection """
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
        else:
            raise ValueError("Data parameter is empty")

    def read(self, query):
        """ Query documents from the collection """
        try:
            results = self.collection.find(query)
            return list(results)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

