#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs."""

from pymongo import MongoClient

mongodb = MongoClient()
logs = mongodb.logs.nginx

count = logs.count_documents({})
get = logs.count_documents({"method": "GET"})
post = logs.count_documents({"method": "POST"})
put = logs.count_documents({"method": "PUT"})
patch = logs.count_documents({"method": "PATCH"})
delete = logs.count_documents({"method": "DELETE"})

status = logs.count_documents({"method": "GET", "path": "/status"})
documents = [get, post, put, patch, delete]

if __name__ == "__main__":
    print(f"{count} logs")
    print("Methods:")

    for method in documents:
        print(f"\tmethod GET: {get}")
        print(f"\tmethod POST: {post}")
        print(f"\tmethod PUT: {put}")
        print(f"\tmethod PATCH: {patch}")
        print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
