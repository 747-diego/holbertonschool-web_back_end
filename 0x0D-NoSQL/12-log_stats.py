#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


if __name__ == "__main__":
    localhost = MongoClient('mongodb://127.0.0.1:27017')
    dependencies = localhost.logs.nginx
    docuLogs = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('{} logs'.format(dependencies.count_documents({})))
    print("Methods:")
    for packages in docuLogs:
        print('\tmethod {}: {}'.format(
            packages, dependencies.count_documents({'method': packages})))
    print('{} status check'.format(
        dependencies.count_documents({'path': '/status'})))
