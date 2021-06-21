#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('{} logs'.format(collection.count_documents({})))
    print("Methods:")
    for i in method:
        print('\tmethod {}: {}'.format(
            i, collection.count_documents({'method': i})))
    print('{} status check'.format(
        collection.count_documents({'path': '/status'})))
