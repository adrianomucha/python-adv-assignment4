from pymongo import MongoClient

client = MongoClient()
test_object = {'a': '1', 'b':'2','c':'3'}
my_collection = client.test_object.my_collection
my_collection.insert(test_object)

def find_object(primary_key):
        """Finds and returns an object matching the primary key.
    Returns None if not found.
    """
    test_object = my_collection.find_one(test_object)
    print(test_object)

def update_object(new_object):
    """Update an object if exists, inster if it does not exists.
    """
    if my_database is None:
        raise ValueError('It does not exists!')
    my_database['details'].append({'d': '4'})
    my_collection.update({'name':'' }, test_object)

def remove_object(primary_key):
        """Delete the object matching primary key.
    Returns True if deleted, False if not found.
    """
pass

find_object(test_object)
    return test_object
